from src.models import Horse
from src.repos import UserRepo, HorseRepo, BetRepo

class RepoService:
    def __init__(self, user_repo, horse_repo, bet_repo):
        self.__user_repo: UserRepo = user_repo
        self.__horse_repo: HorseRepo = horse_repo
        self.__bet_repo: BetRepo = bet_repo

    def check_horses(self) -> list[Horse]: pass