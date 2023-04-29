from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandStrategy import CommandStrategy
from modules.douyin.framework.enums.CommandEnum import CommandEnum


class DemoCommand(CommandStrategy):
    """命令demo的执行策略"""

    def execute(self, command: Command):
        cmd = command.cmd_str.split()[1]
        self.demoSingleSplider(cmd)
        self.demoBatchSplider(cmd)

    @staticmethod
    def demoSingleSplider(cmd):
        if CommandEnum.DOUYINSINGLESPIDER.value == cmd:
            tips = '''
                    *************************************************************************************************************
                        抖音分享视频下载：  可以输入单个链接，也可输入多个链接，多个链接使用英文（,）隔开。
                        单个链接示例： dys https://www.douyin.com/video/6985373969901702440
                        多个链接示例： dys https://www.douyin.com/video/6985373969901702440,https://www.douyin.com/video/7219982529795869987
                    *************************************************************************************************************
                    '''
            print(tips)

    @staticmethod
    def demoBatchSplider(cmd):
        if CommandEnum.DOUYINBATCHSPIDER.value == cmd:
            tips = '''
                    *************************************************************************************************************
                        抖音博主视频下载：  可以输入单个链接，也可输入多个链接，多个链接使用英文（,）隔开。
                        单个链接示例： dyb https://www.douyin.com/user/MS4wLjABAAAAAgYJ4nk7s8RVwjHbVpMv0AYGFshAO6aJJE4SnrKtKdT_NUGPuu59BjScgpXHGgH4
                        多个链接示例： dyb https://www.douyin.com/user/MS4wLjABAAAAAgYJ4nk7s8RVwjHbVpMv0AYGFshAO6aJJE4SnrKtKdT_NUGPuu59BjScgpXHGgH4,https://www.douyin.com/user/MS4wLjABAAAAAgYJ4nk7s8RVwjHbVpMv0AYGFshAO6aJJE4SnrKtKdT_NUGPuu59BjScgpXHGgHc
                    *************************************************************************************************************
                    '''
            print(tips)
