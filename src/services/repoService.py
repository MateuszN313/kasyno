import hashlib

from src.models import Horse, User, Bet
from src.repos import UserRepo, HorseRepo, BetRepo


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

        password_hash = hashlib.sha256(password.encode()).hexdigest()
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

    def check_bets(self) -> None:
        bets = self.__bet_repo.get_bets()
        for bet in bets:
            print(f"{bet}\n")

    def add_bet(self, bet: Bet) -> None:
        self.__bet_repo.add_bet(bet)

    def remove_bet(self, id: str) -> bool:
        return self.__bet_repo.remove_bet(id)

    def check_horses(self) -> None:
        horses = self.__horse_repo.get_horses()
        for horse in horses:
            print(f"{horse}")

    def remove_horse(self, id: str) -> bool:
        return self.__horse_repo.remove_horse(id)

    def add_horse(self, horse: Horse) -> None:
        self.__horse_repo.add_horse(horse)