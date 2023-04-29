from modules.douyin.framework.command.HelpCommand import HelpCommand
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandHandler import CommandHandler
from modules.douyin.framework.enums.CommandEnum import CommandEnum


class ErrorCommandHandler(CommandHandler):
    """处理error命令的处理者"""

    def support(self, command: Command):
        return True

    def handle(self, command: Command):
        print('错误的指令：' + command.cmd_str)
        HelpCommand().execute(command)
