from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Email: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")


class SlackNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Slack message: {message}")


class NotificationService:
    def __init__(self, notifiers: list[Notifier]):
        self.notifiers = notifiers

    def notify_all(self, message: str):
        for notifier in self.notifiers:
            notifier.send(message)


service = NotificationService(
    [
        EmailNotifier(),
        SlackNotifier(),
        EmailNotifier(),
    ]
)

service.notify_all("Black Friday is coming!")
