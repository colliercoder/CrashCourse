"""Class defining Users"""
class User():
    def __init__(self, username,password,age):
        self.username = username
        self.password = password
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print("The username: "+self.username)
        print("The password: " + self.password)
        print("The user's age: " + str(self.age))
    def greet_user(self):
        print("Hello " + self.username + " and welcome back!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.username + " login attempts: " + str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.username + " login attempts are now set back to " + str(self.login_attempts))



