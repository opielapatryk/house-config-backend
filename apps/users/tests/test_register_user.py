import pytest
from apps.users.application.use_cases import RegisterUser

class FakeUser:
    def __init__(self, email):
        self.email = email

class FakeUserRepo:
    def create_user(self, email, password):
        return FakeUser(email)

def test_register_user():
    repo = FakeUserRepo()
    use_case = RegisterUser(repo)
    user = use_case.execute(email="test@example.com", password="secret123")
    assert user.email == "test@example.com"