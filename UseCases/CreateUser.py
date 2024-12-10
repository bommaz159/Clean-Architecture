from Entities.User import User
from Infrastructure.UserRepository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> str:
        # Kiểm tra xem email đã tồn tại chưa
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            return "User with this email already exists."

        # Tạo người dùng mới
        new_user = User(email=email, password=password)

        # Lưu người dùng vào cơ sở dữ liệu
        self.user_repository.save(new_user)

        return "User created successfully."
