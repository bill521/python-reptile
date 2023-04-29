from modules.douyin.framework.command.DouyinSingleSpiderCommand import DouyinSingleSpiderCommand
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandHandler import CommandHandler
from modules.douyin.framework.enums.CommandEnum import CommandEnum


class DouyinSingleSpiderCommandHandler(CommandHandler):
    """处理dir命令的处理者"""

    def support(self, command: Command):
        cmd_name = command.cmd_str.split()[0]
        return cmd_name == CommandEnum.DOUYINSINGLESPIDER.value

    def handle(self, command: Command):
        if self.support(command):
            DouyinSingleSpiderCommand().execute(command)
        else:
            super().handle(command)
