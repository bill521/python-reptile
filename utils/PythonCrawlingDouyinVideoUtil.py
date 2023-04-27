
import os
import requests
import re

class HttpHeaders:
    def __init__(self, cookie, user_agent):
        self.cookie = cookie
        self.user_agent = user_agent

class PythonCrawlingDouyinVideoUtil:

    def __init__(self, httpHeaders, folder_path):
        self.folder_path = folder_path
        self.headers = {'cookie': httpHeaders.cookie, 'User-Agent': httpHeaders.user_agent}

    # UP主抖音视频爬取类
    def batch_crawling_video(self, url):
         self.printSuccess()


    # 单个抖音视频爬取类
    def single_crawling_video(self, url):
        self.url = url
        self.create_save_video_folder()
        self.requests_get_html()
        self.getTitle()
        self.getVideoUrl()
        self.downloadVideoByVideoUrl()
        self.printSuccess()

    # 发送请求
    def requests_get_html(self):
        self.response = requests.get(url=self.url, headers=self.headers)


    def create_save_video_folder(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = os.path.join(desktop_path, "yujian")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def printSuccess(self):
        self.printInfo("代码执行成功！")

    def printInfo(self, message):
        print(message)

    def getTitle(self):
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', self.response.text)[0]
        self.title = title.replace(" ", "").replace("\n", "")
        self.printInfo(self.title)


    def getVideoUrl(self):
        html_data = re.findall('src(.*?)%26btag%3D', self.response.text)[1]
        self.video_url = requests.utils.unquote(html_data).replace('":"', 'https:')


    def downloadVideoByVideoUrl(self):
        video_content = requests.get(url=self.video_url, headers=self.headers).content
        # 根据url地址下载视频到我们指定的保存路径
        with open(self.folder_path + self.title + '.mp4', mode='wb') as f:
            f.write(video_content)
            print(self.title, self.video_url)

# 调用

httpHeaders  = HttpHeaders("ttwid=1%7CvTO_uJ7LmaveRIOE8nlIwh0MF9NA5UKrFYGNozKNQKM%7C1682424504%7C182d57cf452d8ec06cebbdfab649f8a7251a58db51307e7c24f07f4314e6e675; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=%221682424506.261%22; passport_csrf_token=4517be9174294276aef4a0270de60b9d; passport_csrf_token_default=4517be9174294276aef4a0270de60b9d; msToken=XEm0LWG1_Txdm0MaoS3m4O6eELy4jdlcNg943sZbis_0EemVNRJM3nBOOsGXk03pQbP99vEXufu5hUrBhTH5RAzOvdQIJV2h3OvlSnEkXUo=; __ac_nonce=06447c2cb00b1be795f84; __ac_signature=_02B4Z6wo00f01JB.4VwAAIDAEH0bHpBBnDCQT-XAAEBc4f; __ac_referer=__ac_blank",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3");

crawlingDouyinVideo = PythonCrawlingDouyinVideoMain(httpHeaders, 'video\\')

# crawlingDouyinVideo.batch_crawling_video('https://www.douyin.com/user/MS4wLjABAAAAAgYJ4nk7s8RVwjHbVpMv0AYGFshAO6aJJE4SnrKtKdT_NUGPuu59BjScgpXHGgH4')

crawlingDouyinVideo.single_crawling_video('https://www.douyin.com/video/7223706135776300345')