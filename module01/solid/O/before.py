"""Software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification."""

from abc import ABC, abstractmethod
from enum import Enum


class NotifierType(Enum):
    EMAIL = "email"
    SMS = "sms"
    SLACK = "slack"


class Notifier:
    # still one responsibility you may say
    def send(self, message: str, service=NotifierType.EMAIL):
        # at the beginning there was only email then we decided to extend
        match service:
            case NotifierType.EMAIL:
                print(f"Sending Email: {message}")
            case NotifierType.SMS:
                print(f"Sending SMS: {message}")
            case NotifierType.SLACK:
                print(f"Sending Slack message: {message}")


message = "Black Friday is coming!"
notifier = Notifier()
notifier.send(message)
notifier.send(message, NotifierType.SLACK)
notifier.send(message, NotifierType.SMS)
