"""NIM (4 kyu)

https://www.codewars.com/kata/nim
"""

import random


def choose_move(game_state):
    """Choose a move to play given a game state."""
    x = reduce(lambda a, b: a ^ b, game_state)
    seq = [(i, n ^ x) for i, n in enumerate(game_state) if n ^ x < n]
    if not seq:
        return pick_random(game_state)
    pile, s = min(seq, key=lambda t: t[1])
    return pile, game_state[pile] - s


def pick_random(non_empty_game_state):
    pile, maxi = random.choice(list(enumerate(non_empty_game_state)))
    return pile, random.randint(1, maxi)
