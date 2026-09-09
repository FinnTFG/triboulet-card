from collections import Counter
import random

suits = ["spades", "hearts", "diamonds", "clubs"]
ranks = [(str(i), i) for i in range(2, 11) ]

ranks += [
    ("J",10),
    ("Q",10),
    ("K",10),
    ("A",11)
    ]
    
deck = []

for suit in suits:
    for rank, chips in ranks:
        deck.append({
            "suit": suit,
            "rank": rank,
            "chips": chips
        })
        
random.shuffle(deck)

hand = []

for _ in range(8):
    if len(deck) == 0:
        break
    else:
        pull = deck.pop(0)
        hand.append(pull)
for item_id, item in enumerate(hand, start=1):
    print(f"{item_id} | {item}", "\n")
print("cards left:", len(deck))
print("# of cards in hand:", len(hand), "\n")

choices = input("Choose cards (1-8, 5 max): ")
handIndex = [int(num) - 1 for num in choices.split()]
playedCards = [hand[i] for i in handIndex]
print(*playedCards, sep='\n')

counts = Counter(card["rank"] for card in playedCards)
count_values = sorted(counts.values(), reverse=True)
matches = Counter(count_values)
match_values = sorted(matches.values(), reverse=True)
print(match_values)
