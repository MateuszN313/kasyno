class Card:
    def __init__(self, figure: str, suit: str):
        self.__figure: str = figure
        self.__suit: str = suit

    def get_copy(self):
        return Card(self.__figure, self.__suit)

    def get_figure(self):
        return self.__figure

    def get_suit(self):
        return self.__suit