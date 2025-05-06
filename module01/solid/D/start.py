"""
Dependency Injection is a way to provide dependencies (usually objects) to a class rather than having the class create them itself.
"""


class EmailService:
    def send(self, to: str, subject: str, body: str):
        print(f"Sending email to {to}: {subject}")


class UserService:
    def __init__(self):
        self.email_service = EmailService()  # tightly coupled

    def register_user(self, email: str):
        # ... create user logic ...
        self.email_service.send(email, "Welcome!", "Thanks for registering.")
