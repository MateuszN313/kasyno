from src.models import User
from src.repos import UserRepo

class UserCsvRepo(UserRepo):
    def __init__(self, path):
        self.__users: list[User] = []
        self.__path: str = path
        self._load()

    def add_user(self, user) -> bool:
        pass

    def remove_user(self, user_id) -> bool:
        pass

    def get_users(self) -> list[User]:
        pass

    def get_user(self, user_id) -> User:
        pass

    def _load(self) -> None:
        pass

    def _save(self) -> None:
        pass

