from Infrastructure.UserRepository import UserRepository
from Entities.User import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def find_by_email(self, email: str) -> User:
        return self.users.get(email)

    def save(self, user: User) -> None:
        self.users[user.email] = user
