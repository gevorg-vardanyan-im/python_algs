from design_patterns.Behavioral.Mediator.Chat import Chat
from design_patterns.Behavioral.Mediator.User import User


class Admin(User):
    """docstring for Admin"""

    def __init__(self, name, chat: Chat):
        self.chat = chat
        self.name = name

    def send_message(self, message):
        self.chat.send_message(message, self)

    def get_message(self, message):
        print("{user} is receiving a message\n--- \t'{message}'"
              .format(user=self.name, message=message))
