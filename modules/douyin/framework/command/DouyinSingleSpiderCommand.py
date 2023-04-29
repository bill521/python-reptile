import re
import time

from commons.utils.DouyinMessageUtil import print_info
from commons.utils.ValidDataUtil import valid_data_website
from config.SpiderConfig import SpiderConfig
from modules.douyin.api.DouyinSingleSpider import DouyinSingleSpider
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandStrategy import CommandStrategy


class DouyinSingleSpiderCommand(CommandStrategy):
    """爬取抖音分享的单个视频视频"""

    def execute(self, command: Command):
        if self.valid_data_options(command.cmd_str):
            options = command.cmd_str.split()[1]
            urls = re.split(',', options)
            if self.valid_data_website_all_pass(urls):
                config = SpiderConfig(None, None, None, None)
                douyin_spider_instance = DouyinSingleSpider(config.default_harder())
                print_info(f'数据校验通过，准备下载视频')
                time.sleep(1)
                for url in urls:
                    douyin_spider_instance.crawling_video(url)
                print_info(f'下载任务完成！')

    @staticmethod
    def valid_data_website_all_pass(urls):
        for url in urls:
            if not valid_data_website(url):
                print_info(f'输入的链接:{url}不是正确,请检查抖音分享链接！\n')
                return False
        return True

    @staticmethod
    def valid_data_options(cmd_str):
        if len(cmd_str.split()) > 1:
            return True
        print_info(f'输入的命令：{cmd_str}缺少参数 \n')
        return False