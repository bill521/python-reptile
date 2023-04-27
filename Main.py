from config.SpiderConfig import SpiderConfig
from model.douyin.DouyinSingleSpider import DouyinSpider

def download(up_url):
    config = SpiderConfig(None, None, None)
    douyin_spider_instance = DouyinSpider(config.default_harder())
    douyin_spider_instance.crawling_video(up_url)


# https://www.douyin.com/video/7223706135776300345
if __name__ == '__main__':
    tips = '''
    *************************************************************************************************************
        抖音视频爬虫
        请输入分享链接，可以输入单个链接，也可输入多个链接。
        单个链接示例：https://v.douyin.com/JeUKHSf/
        多个链接示例：https://v.douyin.com/JeUKHSf/，https://v.douyin.com/JeUKHSf/，https://v.douyin.com/JeUKHSf/
        输入exit退出
    *************************************************************************************************************
    '''
    print(tips)
    input_url = input('请输入：')
    while input_url != 'exit':
        download(input_url)
        input_url = input('请输入链接继续或 exit 退出：')
