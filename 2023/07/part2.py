def hand_score(card_count):
    if "J" in card_count and card_count["J"] != 5:
        j_count = card_count["J"]
        card_count.pop("J")
        card_count[max(card_count, key=card_count.get)] += j_count
    counts = list(card_count.values())
    if 5 in counts: # five of a kind
        return 7
    elif 4 in counts: # four of a kind
        return 6
    elif 3 in counts and 2 in counts: # full house
        return 5
    elif 3 in counts: # three of a kind
        return 4
    elif counts.count(2) == 2: # two pair
        return 3
    elif 2 in counts: # one pair
        return 2
    else: # high card
        return 1

def card_count(hand):
    card_count = {}
    for card in hand[0]:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    return card_count

def less_equal_than(hand1, hand2):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    card_count1 = card_count(hand1)
    card_count2 = card_count(hand2)
    hand_score1 = hand_score(card_count1)
    hand_score2 = hand_score(card_count2)
    if hand_score1 < hand_score2:
        return True
    elif hand_score1 > hand_score2:
        return False
    else:
        for i in range(len(hand1[0])):
            if cards.index(hand1[0][i]) < cards.index(hand2[0][i]):
                return False
            elif cards.index(hand1[0][i]) > cards.index(hand2[0][i]):
                return True
        return True

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if less_equal_than(array[j], pivot):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

hands = []
for line in lines:
    cards, bid = line.split(" ")
    hands.append([cards, int(bid)])

quickSort(hands, 0, len(hands) - 1)

total = 0
for i in range(len(hands)):
    total += (i + 1) * hands[i][1]

print(total)