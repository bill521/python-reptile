from config.SpiderConfig import SpiderConfig
from utils.DouyinSpiderUtil import DouyinSpiderUtil


def download(up_url):
    config = SpiderConfig(
        "ttwid=1%7CvTO_uJ7LmaveRIOE8nlIwh0MF9NA5UKrFYGNozKNQKM%7C1682424504"
        "%7C182d57cf452d8ec06cebbdfab649f8a7251a58db51307e7c24f07f4314e6e675; home_can_add_dy_2_desktop=%220%22; "
        "strategyABtestKey=%221682424506.261%22; passport_csrf_token=4517be9174294276aef4a0270de60b9d; "
        "passport_csrf_token_default=4517be9174294276aef4a0270de60b9d; "
        "msToken"
        "=XEm0LWG1_Txdm0MaoS3m4O6eELy4jdlcNg943sZbis_0EemVNRJM3nBOOsGXk03pQbP99vEXufu5hUrBhTH5RAzOvdQIJV2h3OvlSnEkXUo=; "
        "__ac_nonce=06447c2cb00b1be795f84; __ac_signature=_02B4Z6wo00f01JB.4VwAAIDAEH0bHpBBnDCQT-XAAEBc4f; "
        "__ac_referer=__ac_blank",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        None
    )
    douyin_spider_instance = DouyinSpiderUtil(config)
    # 调用爬取单个视频文件方法
    douyin_spider_instance.single_crawling_video(up_url)


# https://www.douyin.com/video/7223706135776300345
if __name__ == '__main__':
    print('*' * 50)
    print('欢迎使用！！！')
    print(
        '请输入类似格式（https://github.com/liangzhuz/python_spider/archive/master.zip）的链接下载文件, 或输入exit退出程序。')
    print('*' * 50)
    input_url = input('请输入：')
    while input_url != 'exit':
        download(input_url)
        url = input('请输入链接继续或 exit 退出：')
