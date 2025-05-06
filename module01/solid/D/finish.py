class EmailService:
    def send(self, to: str, subject: str, body: str):
        print(f"Sending email to {to}: {subject}")


class UserService:
    def __init__(self, email_service: EmailService):  # Injected
        self.email_service = email_service

    def register_user(self, email: str):
        # ... create user logic ...
        self.email_service.send(email, "Welcome!", "Thanks for registering.")
