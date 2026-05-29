import os
import shutil
from pathlib import Path
from typing import Optional, List, Any


class FileSystemTool:
    def read_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File not found - {file_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def write_file(self, file_path: str, content: str) -> str:
        try:
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"File written successfully: {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

    def append_file(self, file_path: str, content: str) -> str:
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(content)
            return f"Content appended to: {file_path}"
        except Exception as e:
            return f"Error appending to file: {str(e)}"

    def delete_file(self, file_path: str) -> str:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return f"File deleted: {file_path}"
            else:
                return f"Error: File not found - {file_path}"
        except Exception as e:
            return f"Error deleting file: {str(e)}"

    def list_directory(self, dir_path: str = '.') -> List[str]:
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                return os.listdir(dir_path)
            else:
                return []
        except Exception as e:
            return []

    def create_directory(self, dir_path: str) -> str:
        try:
            os.makedirs(dir_path, exist_ok=True)
            return f"Directory created: {dir_path}"
        except Exception as e:
            return f"Error creating directory: {str(e)}"

    def delete_directory(self, dir_path: str) -> str:
        try:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
                return f"Directory deleted: {dir_path}"
            else:
                return f"Error: Directory not found - {dir_path}"
        except Exception as e:
            return f"Error deleting directory: {str(e)}"

    def file_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path) and os.path.isfile(file_path)

    def directory_exists(self, dir_path: str) -> bool:
        return os.path.exists(dir_path) and os.path.isdir(dir_path)

    def get_file_size(self, file_path: str) -> Optional[int]:
        try:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                return os.path.getsize(file_path)
            return None
        except Exception:
            return None

    def get_file_modified_time(self, file_path: str) -> Optional[str]:
        try:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                mtime = os.path.getmtime(file_path)
                return str(mtime)
            return None
        except Exception:
            return None
