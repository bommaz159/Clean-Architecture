from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Entities.User import User
from Infrastructure.UserRepository import UserRepository

# Kết nối cơ sở dữ liệu
DATABASE_URL = "mssql+pyodbc://sa:1@LAPTOP-E3NJJ9JU\\SUNSERVER/LTPT?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khởi tạo ORM base
Base = declarative_base()

# ORM Model
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

# Repository với SQLAlchemy
class SQLServerUserRepository(UserRepository):
    def __init__(self):
        Base.metadata.create_all(bind=engine)  # Tạo bảng nếu chưa có
        self.db = SessionLocal()

    def find_by_email(self, email: str) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if db_user:
            return User(email=db_user.email, password=db_user.password)
        return None

    def save(self, user: User) -> None:
        db_user = UserModel(email=user.email, password=user.password)
        self.db.add(db_user)
        self.db.commit()
