class User:
    """Information about user"""

    def __init__(self, first_name, last_name, age, hobby):
        self.name = first_name.title()
        self.last = last_name.title()
        self.age = str(age)
        self.hobby = hobby

    def describe_user(self):
        """Return all information about user"""
        message = f'First name: {self.name}\nLast name: {self.last}\nAge: {self.age}\nHobby: {self.hobby}'
        return message

    def greet_user(self):
        """Return HELLO-message to user"""
        message = f'Hello, {self.name} {self.last}!'
        return message


user1 = User('sanya', 'zalupko', 19, 'none')
user2 = User('oleg', 'nichiparenka', 0, 'read books')
user3 = User('ivan', 'pupkin', 6, 'rap')
print(user3.describe_user() + '\n...')
print(user1.describe_user() + '\n...')
print(user2.describe_user() + '\n...\n')
print(user1.greet_user() + '\n')
print(user2.greet_user() + '\n')
print(user3.greet_user() + '\n')
