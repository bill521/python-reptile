from enum import Enum, unique


@unique
class CommandEnum(Enum):
    # 分享视频
    DOUYINSINGLESPIDER = "dys"
    # 爬取博主视频
    DOUYINBATCHSPIDER = "dyb"
    # 帮助
    HELP = "help"
    # 示例
    DEMO = "demo"
