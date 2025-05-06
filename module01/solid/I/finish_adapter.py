from abc import ABC, abstractmethod


class FileUploader(ABC):
    @abstractmethod
    def upload(self, file_path: str):
        pass


class FileDownloader(ABC):
    @abstractmethod
    def download(self, file_name: str):
        pass


class FileDeleter(ABC):
    @abstractmethod
    def delete(self, file_name: str):
        pass


class FileLister(ABC):
    @abstractmethod
    def list_files(self):
        pass


class S3Storage(FileUploader, FileDownloader, FileDeleter, FileLister):
    def upload(self, file_path: str):
        print(f"Uploading {file_path} to S3")

    def download(self, file_name: str):
        print(f"Downloading {file_name} from S3")

    def delete(self, file_name: str):
        print(f"Deleting {file_name} from S3")

    def list_files(self):
        return ["file1.txt", "file2.txt"]


class ReadOnlyStorage(FileDownloader, FileLister):
    def download(self, file_name: str):
        print(f"Reading {file_name} from archive")

    def list_files(self):
        return ["archived_1.txt"]
