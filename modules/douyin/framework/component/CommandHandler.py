from modules.douyin.framework.component.Command import Command


class CommandHandler:
    """责任链处理者基类"""

    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def handle(self, command: Command):
        if self._next_handler:
            self._next_handler.handle(command)

    def support(self, command: Command):
        pass

