"""Configuration module for the CLI slots game.

This module contains all the game settings and configurations including:
- Slot symbols and their values
- Paylines configuration
- Betting options
- Display settings
"""

# Slot machine symbols with their respective values
SYMBOLS = {
    '🍒': 10,   # Cherry
    '🍋': 20,   # Lemon
    '🍊': 30,   # Orange
    '🍇': 40,   # Grapes
    '💎': 100,  # Diamond
    '🎰': 200,  # Jackpot
}

# Number of reels in the slot machine
NUM_REELS = 3

# Number of visible symbols per reel
VISIBLE_ROWS = 3

# Betting configuration
MIN_BET = 1
MAX_BET = 100
DEFAULT_BET = 10

# Initial player balance
INITIAL_BALANCE = 1000

# Winning combinations (horizontal and diagonal lines)
PAYLINES = [
    # Top row
    [(0, 0), (1, 0), (2, 0)],
    # Middle row
    [(0, 1), (1, 1), (2, 1)],
    # Bottom row
    [(0, 2), (1, 2), (2, 2)],
    # Diagonal from top-left to bottom-right
    [(0, 0), (1, 1), (2, 2)],
    # Diagonal from top-right to bottom-left
    [(2, 0), (1, 1), (0, 2)],
]