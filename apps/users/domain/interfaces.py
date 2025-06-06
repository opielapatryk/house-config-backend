from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str):
        pass