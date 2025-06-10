from apps.users.domain.interfaces import UserRepository
from dataclasses import dataclass

class RegisterUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str, username: str):
        return self.user_repo.create_user(email, password, username)

@dataclass
class LoginResult:
    success: bool
    user: object = None
    error: str = None

class LoginUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        
    def execute(self, email: str, password: str):
        user = self.user_repo.authenticate_user(email, password)
        if user:
            return LoginResult(success=True, user=user)
        return LoginResult(success=False, error="Invalid credentials")