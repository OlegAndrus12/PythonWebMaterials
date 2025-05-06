"""
In this context, a responsibility is considered to be one reason to change.
This principle states that if we have 2 reasons to change for a class,
we have to split the functionality in two classes.
Each class will handle only one responsibility and
if in the future we need to make one change we are going to make it in the class which handles it.
When we need to make a change in a class having more responsibilities the change might affect the other
functionality related to the other responsibility of the class.

The Single Responsibility Principle is a simple and intuitive principle,
but in practice it is sometimes hard to get it right.
"""

from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager(FileManager):
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
