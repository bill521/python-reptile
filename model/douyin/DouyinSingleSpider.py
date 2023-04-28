import os
import requests
import re

from model.base.AbstractSpider import AbstractSlider


class DouyinSingleSpider(AbstractSlider):

    def __init__(self, crawling_config):
        AbstractSlider.__init__(self, crawling_config)
        self.title = None
        self.video_url = None
        self.response = None
        self.url = None

    # 单个抖音视频爬取类
    def crawling_video(self, url):
        self.url = url
        AbstractSlider.create_save_video_folder(self)
        self.requests_get_html()
        self.get_title()
        self.get_video_url()
        self.download_video_by_video_url()

    # 发送请求
    def requests_get_html(self):
        self.response = requests.get(url=self.url, headers=self.headers)

    def get_title(self):
        title = re.findall('<title data-react-helmet="true">([\s\S]*?)</title>', self.response.text)[0]
        self.title = title.replace(" ", "").replace("\n", "")

    def get_video_url(self):
        video_list = re.findall('src(.*?)%26btag%3D', self.response.text)
        # 优化：检索的视频字典为空的情况
        if len(video_list) > 0:
            html_data = video_list[1]
            self.video_url = requests.utils.unquote(html_data).replace('":"', 'https:')

    def download_video_by_video_url(self):
        print(self.url, self.title, self.video_url)
        video_content = requests.get(url=self.video_url, headers=self.headers).content
        with open(self.folder_path + os.path.sep + self.title + '.mp4', mode='wb') as f:
            f.write(video_content)
            