"""

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456


"""
from collections import defaultdict
import functools

card_types = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")


def compare_hands(hand1, hand2):
    for i in range(len(hand1)):
        if card_types.index(hand1[i]) < card_types.index(hand2[i]):
            return -1
        elif card_types.index(hand1[i]) > card_types.index(hand2[i]):
            return 1
    return 0


def part1(file):
    # Could use regex

    combos = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]

    hands = ["Five_Of_A_Kind", "Four_Of_A_Kind", "Full House", "Three_Of_A_Kind", "Two Pair", "One Pair", "High Card"]

    players = []
    for index, line in enumerate(file):
        players.append(line.strip("\n").split(" "))

    player_hand = defaultdict(list)
    for i, player in enumerate(players):
        card_combo = defaultdict(int)
        hand = player[0]
        for card in hand:
            card_combo[card] += 1
        for index, combo in enumerate(combos):
            if combo == sorted(list(card_combo.values())):
                player_hand[index].append([i, player[0]])

    i = 0
    score = 0
    position = 0
    check = []
    while i < len(combos):
        if player_hand.get(i) is not None:
            if len(player_hand.get(i)) == 1:
                player_index = player_hand.get(i)[0][0]
                player_bet = players[player_index][1]
                rank = (len(players) - position)
                score += rank * int(player_bet)
                position += 1
                check.append(players[player_index][0])
            else:
                sorted_hands = sorted(list(player_hand.get(i)),
                                      key=functools.cmp_to_key(lambda x, y: compare_hands(x[1], y[1])))
                for hand in sorted_hands:
                    rank = (len(players) - position)
                    player_bet = players[hand[0]][1]
                    score += rank * int(player_bet)
                    position += 1
                    check.append(players[hand[0]][0])
        i += 1

    print(score)

def part2(file):
    print("Qwer")


with open("input.txt", "r") as file:
    part1(file)
    # part2(file)
