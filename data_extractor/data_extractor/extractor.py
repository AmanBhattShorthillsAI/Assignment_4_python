from abc import ABC, abstractmethod


class Extractor(ABC):
    def __init__(self, loader, file_path):
        self.file = loader.load_file(file_path)
        self.file_path = file_path

    @abstractmethod
    def extract_text(self):
        pass

    @abstractmethod
    def extract_images(self):
        pass

    @abstractmethod
    def extract_urls(self):
        pass

    @abstractmethod
    def extract_tables(self):
        pass
