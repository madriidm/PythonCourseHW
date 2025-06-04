# Detyra 5
from random import randrange, randint

# Exercise 1: Random Password
def random_password():
    length = randint(7, 10)
    result = ""
    for _ in range(length):
        result += chr(randint(33, 126))
    return result

# Exercise 2: Random Lottery Numbers
def lottery_numbers():
    min_num = 1
    max_num = 49
    num_nums = 6
    ticket_nums = []
    while len(ticket_nums) < num_nums:
        rand = randint(min_num, max_num)
        if rand not in ticket_nums:
            ticket_nums.append(rand)
    ticket_nums.sort()
    print("Lottery numbers:", ticket_nums)

# Exercise 3: Shuffle a Deck of Cards
def create_deck():
    cards = []
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            cards.append(value + suit)
    return cards

def shuffle(cards):
    for i in range(len(cards)):
        j = randrange(len(cards))
        cards[i], cards[j] = cards[j], cards[i]

def main():
    print("Random Password:", random_password())
    lottery_numbers()

    cards = create_deck()
    print("Original deck:", cards)
    shuffle(cards)
    print("Shuffled deck:", cards)

if __name__ == "__main__":
    main()
