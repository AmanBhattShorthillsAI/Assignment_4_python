from pptx import Presentation
from data_extractor.file_loaders.file_loader import FileLoader

class PPTLoader(FileLoader):
    def load_file(self, file_path: str) -> Presentation:
        return super().load_file(file_path, Presentation)