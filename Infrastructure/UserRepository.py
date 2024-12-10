from abc import ABC, abstractmethod
from Entities.User import User

class UserRepository(ABC):
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
