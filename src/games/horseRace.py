import random
from src.games import Game
from src.models import Horse

class HorseRace(Game):
    def __init__(self, horses: list[Horse]):
        self.__horses: list[Horse] = horses

    def get_horses(self) -> list[Horse]:
        return list(self.__horses)

    def play(self, value: float, user_balance: float) -> float:
            """
            !!!BARDZO WAŻNE!!!
            na ten moment zrobilem tak ze gracz stawia kase i gra losuje konia za niego
            bo szczerze to nie wiem czy to sie da zrobic nie zmieniajac gameservice ale mozna
            zrobic cos takiego ze jesli wybierze wyscig koni to odpali race() i bedzie mogl wybrac konia
            a jak inna gra blackjack to uzyje play() ale nw musze zobaczyc
            """
            if not self.__horses:
                raise ValueError("Brak koni do wyścigu!")
            chosen = random.choice(self.__horses)
            winner, multiplier = self.race(chosen.get_id())
            return multiplier

    def race(self, chosen_horse_id: str) -> tuple[Horse, float]:
        if not self.__horses:
            raise ValueError("Brak koni do wyścigu")

        winner = random.choices(
            self.__horses,
            weights=[h.calculate_winrate() for h in self.__horses])[0]
        chosen = next((h for h in self.__horses if h.get_id() == chosen_horse_id), None)

        if chosen is None:
            return winner, -1.0

        if winner.get_id() == chosen_horse_id:
            multiplier = round(100 / chosen.calculate_winrate(), 2)
            return winner, multiplier
        else:
            return winner, -1.0

    def retire_horse_if_needed(self, horse: Horse) -> Horse | None:
        if horse.needs_retirement():
            new_horse = Horse()
            index = next((i for i, h in enumerate(self.__horses) if h.get_id() == horse.get_id()), None)
            if index is not None:
                self.__horses[index] = new_horse
            return new_horse
        return None
