from django.contrib.auth import get_user_model, authenticate
from apps.users.domain.interfaces import UserRepository

class DjangoUserRepository(UserRepository):
    def create_user(self, email: str, password: str, username: str):
        return get_user_model().objects.create_user(email=email, password=password, username=username)
        
    def authenticate_user(self, email: str, password: str):
        """
        Authenticates a user with the provided email and password
        Returns the User object if successful, None otherwise
        """
        return authenticate(username=email, password=password)
    