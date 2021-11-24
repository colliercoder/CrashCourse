from users import User

"""Class defining Admins"""
class Admin(User):
    def __init__(self, username, password, age):
        super().__init__(username, password, age)
        self.privileges = Privileges()

"""Class defining privileges"""
class Privileges():
    def __init__(self,privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are the admin's privelages: ")
        if self.privileges:
            for i, privilege in enumerate(self.privileges):
                print(str(i+1) + ' ' + privilege.title())
        else:
            print("This user has no privileges")