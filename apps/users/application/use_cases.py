from apps.users.domain.interfaces import UserRepository

class RegisterUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str, username: str):
        return self.user_repo.create_user(email, password, username)