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


increment_msg = '+1 login attempt'
user1 = User('sanya', 'zalupko', 19, 'none')
print(f'Login attempts: {str(user1.login_attempts)}')
user1.increment_login_attempts()
print(increment_msg)
user1.increment_login_attempts()
print(increment_msg)
user1.increment_login_attempts()
print(increment_msg)
print(f'Login attempts: {str(user1.login_attempts)}')
user1.reset_login_attempts()
print('Login attempts was reset')
print(f'Login attempts: {str(user1.login_attempts)}')
