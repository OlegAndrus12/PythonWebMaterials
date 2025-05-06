"""
The Interface Segregation Principle (ISP) emphasizes the importance of
keeping interfaces slim and relevant to the clients that implement them.
It's one of the SOLID principles, a set of design principles in object-oriented
 software development aimed at making  software designs more understandable,
 flexible, and maintainable.
"""

"""
"Clients should not be forced to depend on methods they do not use."
In simpler terms: split big, bloated interfaces into smaller, role-specific ones.

"""

# ніхто не стриже волосся бензопилою. Можна, але нашо? Це зловживання.
# кожну задачу потрібно вирішувати малою кровю.


class FileStorage:
    def upload(self, file_path: str):
        pass

    def download(self, file_name: str):
        pass

    def delete(self, file_name: str):
        pass

    def list_files(self):
        pass


class ReadOnlyStorage(FileStorage):
    def upload(self, file_path: str):
        raise NotImplementedError("Read-only storage")

    def download(self, file_name: str):
        print(f"Downloading {file_name}")

    def delete(self, file_name: str):
        raise NotImplementedError("Read-only storage")

    def list_files(self):
        return ["archived_1.txt", "archived_2.txt"]
