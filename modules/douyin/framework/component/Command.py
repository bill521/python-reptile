import re

class Command:
    """命令对象"""

    def __init__(self, cmd_str):
        self.cmd_str = cmd_str
