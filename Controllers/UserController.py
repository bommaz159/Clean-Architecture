
from UseCases.CreateUser import CreateUserUseCase

class UserController:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    def create_user(self, email: str, password: str):
        result = self.create_user_use_case.execute(email, password)
        print(result)
