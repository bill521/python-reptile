from commons.utils.DouyinMessageUtil import print_info
from modules.douyin.framework.command.HelpCommand import HelpCommand
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandHandler import CommandHandler
from modules.douyin.framework.enums.CommandEnum import CommandEnum


class HelpCommandHandler(CommandHandler):
    """处理help命令的处理者"""

    def support(self, command: Command):
        cmd_name = command.cmd_str.split()[0]
        return CommandEnum.HELP.value == cmd_name.lower()

    def handle(self, command: Command):
        if self.support(command):
            HelpCommand().execute(command)
        else:
            super().handle(command)
