"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.Mediator.Admin import Admin
from design_patterns.Behavioral.Mediator.OrdinaryUser import OrdinaryUser
from design_patterns.Behavioral.Mediator.TextChat import TextChat


def main():
    text_chat = TextChat()
    admin = Admin('Admin', text_chat)
    first_user = OrdinaryUser('First user', text_chat)
    second_user = OrdinaryUser('Second user', text_chat)

    text_chat.set_admin(admin)
    text_chat.add_user(first_user)
    text_chat.add_user(second_user)

    print('\n\n\t\t chat is active \t\t')
    first_user.send_message('Hello from the first user.')
    print('\n\n\t\t chat is active \t\t')
    second_user.send_message('Hi from the second user.')
    print('\n\n\t\t chat is active \t\t')
    admin.send_message('Hello from the admin.')


if __name__ == '__main__':
    main()
