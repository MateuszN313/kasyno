from src.models import Horse, User
from src.repos import UserRepo, HorseRepo, BetRepo
from src.services import HashService


class RepoService:
    def __init__(self, user_repo, horse_repo, bet_repo):
        self.__user_repo: UserRepo = user_repo
        self.__horse_repo: HorseRepo = horse_repo
        self.__bet_repo: BetRepo = bet_repo

    def check_users(self) -> list[User]:
        return self.__user_repo.get_users()

    def add_user(self, user: User) -> bool:
        return self.__user_repo.save_user(user)

    def remove_user(self, id: str) -> bool:
        return self.__user_repo.remove_user(id)

    def authenticate_user(self, login: str, password: str) -> User | None:
        user = self.__user_repo.get_user_by_login(login)
        if user is None:
            return None

        password_hash = HashService.hash(password)
        if user.get_password_hash() == password_hash:
            return user
        return None

    def change_user_balance(self, id: str, amount: float) -> bool:
        user = self.__user_repo.get_user_by_id(id)
        if user is None:
            return False

        balance = user.get_balance()
        if amount < 0 and balance < abs(amount):
            return False

        user.set_balance(balance + amount)
        return self.__user_repo.save_user(user)