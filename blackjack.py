import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("two", "three", "four", "five", "six", "eight",
         "nine", "ten", "jack", "queen", "king", "ace")
values = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
          "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}
playing = True  # use as well while True. its the same thing

# creating card classes with attributes rank, suit


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # will output cards in order of rank and suit.
        return self.rank + " of "+self.suit

# creating deck classes


class Deck():
    def __init__(self):
        self.deck = []  # start with empty list
        for suit in suits:
            for rank in ranks:
                # grab a card and then add another to the deck
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: "+deck_comp

    def shuffle(self):
        # we don't need to return anything so we ignore return keyword because we aer just shuffling
        random.shuffle(self.deck)

    def deal(self):
        # get the card from this card and pop off a single card then return it.
        single_card = self.deck.pop()
        return single_card


test_deck = Deck()  # create a deck attribute
# shuffle the deck after creating the deck attribute or ignore if you want cards arranged in order.
test_deck.shuffle()
print(test_deck)
