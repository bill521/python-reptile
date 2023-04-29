from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandStrategy import CommandStrategy


class HelpCommand(CommandStrategy):
    """help命令的执行策略"""

    def execute(self, command: Command):
        print("指令列表：")
        print("dys options: 抖音分享视频下载，多个视频链接使用英文(,)分开")
        print("dyb options：抖音博主首页视频下载，多个博主链接使用英文(,)分开")
        print("demo options：查看命令演示示例：demo dys")
        print("exit：退出程序")
