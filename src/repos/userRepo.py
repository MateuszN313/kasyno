from abc import ABC, abstractmethod

from src.models import User

class UserRepo(ABC):
    @abstractmethod
    def add_user(self, user) -> bool: pass

    @abstractmethod
    def remove_user(self, user_id) -> bool: pass

    @abstractmethod
    def get_users(self) -> list[User]: pass

    @abstractmethod
    def get_user(self, user_id) -> User: pass

    @abstractmethod
    def _load(self) -> None: pass

    @abstractmethod
    def _save(self) -> None: pass