import os
import requests
import re

from model.base.AbstractSpider import AbstractSlider
from utils.DouyinFileUtil import create_folder
from utils.DouyinMessageUtil import print_success


class DouyinSingleSpider(AbstractSlider):

    def __init__(self, crawling_config):
        self.title = None
        self.video_url = None
        self.response = None
        self.url = None
        self.folder_path = crawling_config.folder_path
        self.headers = {'cookie': crawling_config.cookie, 'User-Agent': crawling_config.user_agent}

    # 单个抖音视频爬取类
    def crawling_video(self, url):
        self.url = url
        self.create_save_video_folder()
        self.requests_get_html()
        self.get_title()
        self.get_video_url()
        self.download_video_by_video_url()
        print_success()

    # 发送请求
    def requests_get_html(self):
        self.response = requests.get(url=self.url, headers=self.headers)

    def create_save_video_folder(self):
        if self.folder_path is None:
            self.default_create_folder()
        else:
            create_folder(self.folder_path)

    # 默认保存到相对路径
    def default_create_folder(self):
        folder_path = os.path.join("video")
        create_folder(folder_path)
        self.folder_path = folder_path

    def get_title(self):
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', self.response.text)[0]
        self.title = title.replace(" ", "").replace("\n", "")

    def get_video_url(self):
        video_list = re.findall('src(.*?)%26btag%3D', self.response.text)
        # 优化：检索的视频字典为空的情况
        if len(video_list) > 0:
            html_data = video_list[1]
            self.video_url = requests.utils.unquote(html_data).replace('":"', 'https:')

    def download_video_by_video_url(self):
        video_content = requests.get(url=self.video_url, headers=self.headers).content
        with open(self.folder_path + os.path.sep + self.title + '.mp4', mode='wb') as f:
            print(self.url, self.title, self.video_url)
            f.write(video_content)
