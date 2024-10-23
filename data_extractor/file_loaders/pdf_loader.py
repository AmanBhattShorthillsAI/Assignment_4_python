from PyPDF2 import PdfReader
from data_extractor.file_loaders.file_loader import FileLoader


class PDFLoader(FileLoader):
    def load_file(self, file_path) -> PdfReader:
        return super().load_file(file_path, PdfReader)
