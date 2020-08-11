from design_patterns.Behavioral.Mediator.Chat import Chat
from design_patterns.Behavioral.Mediator.User import User


class TextChat(Chat):
    """docstring for TextChat"""

    admin: User
    users = list()

    def set_admin(self, admin: User):
        self.admin = admin

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message, user):
        for u in self.users:
            if u is not user:
                u.get_message(message)
        self.admin.get_message(message=message)
