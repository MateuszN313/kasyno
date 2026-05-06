import random

from src.config.paths import RESOURCES_DIR
from src.models import Card

class DeckOfCards:
    def __init__(self):
        self.__cards: list[Card] = []
        self.__index = 0
        self.__load()

    def get_card(self) -> Card:
        card = self.__cards[self.__index].get_copy()
        self.__index += 1
        return card

    def shuffle(self) -> None:
        random.shuffle(self.__cards)
        self.__index = 0

    def __load(self) -> None:
        file = open(RESOURCES_DIR / "cards.csv", "r")
        for line in file:
            string = line.strip()
            tokens = string.split(";")
            self.__cards.append(Card(tokens[0], tokens[1]))
        file.close()
