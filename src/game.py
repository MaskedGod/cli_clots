"""Core game logic for the CLI slots game.

This module handles the slot machine mechanics including:
- Reel spinning and symbol generation
- Win condition checking
- Payout calculation
"""

from random import choice
from typing import List, Tuple

from .config import SYMBOLS, NUM_REELS, VISIBLE_ROWS, PAYLINES, MIN_BET, INITIAL_BALANCE


class SlotMachine:
    def __init__(self):
        self.symbols = list(SYMBOLS.keys())
        self.reels = self._generate_reels()
        self.balance = INITIAL_BALANCE

    def _generate_reels(self) -> List[List[str]]:
        """Generate initial state for all reels."""
        return [
            [choice(self.symbols) for _ in range(VISIBLE_ROWS)]
            for _ in range(NUM_REELS)
        ]

    def validate_bet(self, bet: int) -> bool:
        """Validate if the bet amount is within limits and player's balance.

        Args:
            bet: The amount player wants to bet

        Returns:
            bool: True if bet is valid, False otherwise
        """
        return MIN_BET <= bet <= self.balance

    def spin(self, bet: int) -> Tuple[List[List[str]], bool]:
        """Spin all reels and return new symbols if bet is valid.

        Args:
            bet: The amount player wants to bet

        Returns:
            Tuple containing reels state and bet validity
        """
        if not self.validate_bet(bet):
            return self.reels, False

        self.balance -= bet
        self.reels = self._generate_reels()
        return self.reels, True

    def check_wins(self, bet: int) -> Tuple[int, List[List[Tuple[int, int]]]]:
        """Check for winning combinations and calculate total win amount.

        Returns:
            Tuple containing total win amount and list of winning paylines.
        """
        total_win = 0
        winning_lines = []

        for line in PAYLINES:
            symbols = [self.reels[x][y] for x, y in line]
            if len(set(symbols)) == 1:  # All symbols in line are the same
                symbol = symbols[0]
                win_amount = SYMBOLS[symbol] * bet
                total_win += win_amount
                winning_lines.append(line)

        self.balance += total_win
        return total_win, winning_lines
