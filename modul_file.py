from comodul_file import User


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
