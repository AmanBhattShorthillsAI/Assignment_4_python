from docx import Document
from data_extractor.file_loaders.file_loader import FileLoader

class DOCXLoader(FileLoader):
    def load_file(self, file_path: str) -> Document:
        return super().load_file(file_path, Document)