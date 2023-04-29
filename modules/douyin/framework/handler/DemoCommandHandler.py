from modules.douyin.framework.command.DemoCommand import DemoCommand
from modules.douyin.framework.component.Command import Command
from modules.douyin.framework.component.CommandHandler import CommandHandler
from modules.douyin.framework.enums.CommandEnum import CommandEnum


class DemoCommandHandler(CommandHandler):

    def support(self, command: Command):
        cmd_name = command.cmd_str.split()[0]
        return cmd_name == CommandEnum.DEMO.value

    def handle(self, command: Command):
        if self.support(command):
            DemoCommand().execute(command)
        else:
            super().handle(command)
