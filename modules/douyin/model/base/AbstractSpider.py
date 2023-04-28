from abc import ABC, abstractmethod
import os
from commons.utils.DouyinFileUtil import create_folder


class AbstractSlider(ABC):

    def __init__(self, crawling_config):
        self.folder_path = crawling_config.folder_path
        self.headers = {'cookie': crawling_config.cookie, 'User-Agent': crawling_config.user_agent}

    @abstractmethod
    def crawling_video(self, url):
        pass

    def create_save_video_folder(self):
        if self.folder_path is None:
            self.default_create_folder()
        else:
            create_folder(self.folder_path)

    # 默认保存到相对路径
    def default_create_folder(self):
        folder_path = os.path.join("video")
        create_folder(folder_path)
        self.folder_path = folder_path
