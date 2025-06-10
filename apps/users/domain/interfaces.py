from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str, username: str):
        pass
        
    @abstractmethod
    def authenticate_user(self, email: str, password: str):
        pass