from abc import ABC, abstractmethod

from src.models import User

class UserRepo(ABC):
    @abstractmethod
    def save_user(self, user: User) -> bool: pass

    @abstractmethod
    def remove_user(self, id: str) -> bool: pass

    @abstractmethod
    def get_users(self) -> list[User]: pass

    @abstractmethod
    def get_user_by_id(self, id: str) -> User: pass

    @abstractmethod
    def get_user_by_login(self, login: str) -> User: pass

    @abstractmethod
    def _load(self) -> None: pass

    @abstractmethod
    def _save(self) -> None: pass