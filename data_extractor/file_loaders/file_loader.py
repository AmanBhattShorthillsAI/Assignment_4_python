from abc import ABC, abstractmethod
from typing import Any

class FileLoader(ABC):
    @abstractmethod
    def load_file(self, file_path, object) -> Any:
        try:
            # Attempt to load the file
            file = object(file_path)
            return file
        except Exception:
            # Catch any exception related to loading the file and raise the expected error
            raise ValueError("Invalid file.")
