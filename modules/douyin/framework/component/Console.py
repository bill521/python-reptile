
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.handler.DemoCommandHandler import DemoCommandHandler
from modules.douyin.framework.handler.DouyinBatchSpiderCommandHandler import DouyinBatchSpiderCommandHandler
from modules.douyin.framework.handler.DouyinSingleSpiderCommandHandler import DouyinSingleSpiderCommandHandler
from modules.douyin.framework.handler.ErrorCommandHandler import ErrorCommandHandler
from modules.douyin.framework.handler.HelpCommandHandler import HelpCommandHandler


class Console:
    """控制台类"""

    def __init__(self):
        self._command_handler = DouyinBatchSpiderCommandHandler(DouyinSingleSpiderCommandHandler(HelpCommandHandler(DemoCommandHandler(ErrorCommandHandler()))))

    def run(self):

        tips = '''
        *************************************************************************************************************
            欢迎使用WJ小工具
            输入help
            输入demo options 查看实例 : demo dys
            输入exit退出
        *************************************************************************************************************
        '''
        print(tips)

        while True:
            print("请输入指令：")
            command = Command(input())
            if command.cmd_str == "exit":
                break
            self._command_handler.handle(command)
