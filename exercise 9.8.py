class User:
    """Information about user"""

    def __init__(self, first_name, last_name, age, hobby):
        self.name = first_name.title()
        self.last = last_name.title()
        self.age = str(age)
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        """Return all information about user"""
        message = f'First name: {self.name}\nLast name: {self.last}\nAge: {self.age}\nHobby: {self.hobby}'
        return message

    def greet_user(self):
        """Return HELLO-message to user"""
        message = f'Hello, {self.name} {self.last}!'
        return message

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:

    def __init__(self):
        self.privileges = ['можно банить пользователей', "можно удалять пользователей", "можно добавлять пользователей",
                           "можно удалять сообщения"]

    def show_privileges(self):
        print("Ваши полномочия:")
        for privilege in self.privileges:
            print(f'- {privilege}')


class Admin(User):

    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()


sanya = Admin('sanya', 'voron', 0, 'rap')
sanya.privileges.show_privileges()
