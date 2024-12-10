from Infrastructure.SQLServerUserRepository import SQLServerUserRepository
from UseCases.CreateUser import CreateUserUseCase
from Controllers.UserController import UserController

# Tạo repository sử dụng SQL Server
user_repository = SQLServerUserRepository()

# Tạo use case
create_user_use_case = CreateUserUseCase(user_repository)

# Tạo controller
user_controller = UserController(create_user_use_case)

# Gọi controller để tạo người dùng
user_controller.create_user("test1@example.com", "password12354")  # User created successfully.
