import random
from random import shuffle

houses = ["♤", "♧", "♡", "♢"]
card_numbers = ["ace", "2", "3", "4", "5", "6", "7", "8", "10", "Jack", "Queen", "King"]
cards = []

for color in houses:
    for number in card_numbers:
        cards.append((color + number))

cards.append("joker")
cards.append("JOKER")

shuffle(cards)

print(f"{cards} aantal: {len(cards)}")

for x in range(7):
    picked = cards.pop(0)
    print(f"kaart: {x + 1} {picked}" )

print(f"{cards} aantal: {len(cards)}")