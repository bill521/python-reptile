from modules.douyin.framework.component.Command import Command


class CommandStrategy:
    """命令执行策略接口"""

    def execute(self, command: Command):
        pass


