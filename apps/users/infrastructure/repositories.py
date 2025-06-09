from django.contrib.auth import get_user_model
from apps.users.domain.interfaces import UserRepository

class DjangoUserRepository(UserRepository):
    def create_user(self, email: str, password: str, username: str):
        return get_user_model().objects.create_user(email=email, password=password, username=username)