from .models import User

class UserRepository:
    def get_all_users(self):
        return User.objects.all()
    
    def add_user(self, name, email):
        user = User(name=name, email=email)
        user.save()
        return user