from src.games import Game
from src.services import DeckOfCards

class Blackjack(Game):
    def __init__(self, deck_of_cards):
        self.__deck_of_cards: DeckOfCards = deck_of_cards

    def play(self) -> float:
        pass
