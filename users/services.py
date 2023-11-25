from .repositories import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_users(self):
        return self.repository.get_all_users()
    
    def create_user(self, name, email):
        return self.repository.add_user(name, email)