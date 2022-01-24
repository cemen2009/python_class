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
        if self.hobby.lower() == 'none':
            message = f'First name: {self.name}\nLast name: {self.last}\nAge: {self.age}\nNo hobby'
        else:
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
