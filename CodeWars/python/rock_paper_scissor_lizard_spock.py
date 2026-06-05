"""
Rock, Paper, Scissors, Lizard, Spock
https://www.codewars.com/kata/rock-paper-scissors-lizard-spock
Topic: Logic

Rules (each beats the two listed):
  Scissors → Paper, Lizard
  Paper     → Rock, Spock
  Rock      → Lizard, Scissors
  Lizard    → Spock, Paper
  Spock     → Scissors, Rock
"""

_BEATS = {
    "scissors": {"paper", "lizard"},
    "paper":    {"rock", "spock"},
    "rock":     {"lizard", "scissors"},
    "lizard":   {"spock", "paper"},
    "spock":    {"scissors", "rock"},
}


def result(p1: str, p2: str) -> str:
    p1, p2 = p1.lower(), p2.lower()
    if p1 not in _BEATS or p2 not in _BEATS:
        return "Oh, Unknown Thing"
    if p1 == p2:
        return "Draw!"
    if p2 in _BEATS[p1]:
        return "Player 1 won!"
    return "Player 2 won!"
