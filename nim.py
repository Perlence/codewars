"""NIM (4 kyu)

https://www.codewars.com/kata/nim
"""

import random


def choose_move(game_state):
    """Choose a move to play given a game state."""
    snegs = sorted(non_empty_piles(game_state), key=lambda (a, b): b)
    if should_give_up(snegs):
        return pick_random(snegs)


def non_empty_piles(game_state):
    return [(i, n) for i, n in enumerate(game_state) if n > 0]


def should_give_up(non_empty_game_state):
    gs = [n for _, n in non_empty_game_state]
    if len(gs) == 1:
        return False
    if len(gs) == 2:
        return gs[0] == gs[1]
    if len(gs) == 3:
        p0, p1, p2 = gs
        if p0 == 1:
            return p1 % 2 == 0 and p2 == p1 + 1


def pick_random(non_empty_game_state):
    pile, maxi = random.choice(non_empty_game_state)
    return pile, random.randint(1, maxi)
