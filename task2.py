from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def consumption(self):
        consumption = self.size/6.5 + 0.5
        return consumption


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        consumption = 2 * self.height + 0.3
        return consumption


coat = Coat(40)
suit = Suit(1.6)

print(coat.consumption)
print(suit.consumption)
print(coat.consumption + suit.consumption)