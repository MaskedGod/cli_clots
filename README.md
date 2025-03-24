# CLI Slots Game

```
  .---------------.
  |  CLI SLOTS!   |
  |   _________   |
  |  |🎰 💎 🍒|  |
  |  |🍊 🎰 🍇|  |
  |  |🍋 💎 🍊|  |
  |   ‾‾‾‾‾‾‾‾‾   |
  |   [SPIN!]     |
  '---------------'
```

A simple yet engaging command-line interface slot machine game with animated reels, betting system, and multiple winning combinations.

## Features

- Animated slot machine reels with smooth spinning animation
- Multiple symbols with different payout values
- 5 winning paylines (3 horizontal + 2 diagonal)
- Flexible betting system with balance-based limits
- Real-time balance tracking and win calculations
- Visual highlighting of winning combinations
- Initial balance of $1000 to start playing

## Installation

No dependencies required! Just clone this repository and run the game using Python 3.12 or higher.

## How to Play

1. Run the game:

   ```bash
   python main.py
   ```

2. Game Controls:

   - Press 'b' to set bet amount (1-100, limited by your current balance)
   - Press 's' to spin the reels
   - Press 'q' to quit the game

3. Gameplay Rules:
   - Start with $1000 initial balance
   - Place bets within your current balance limit
   - Win by matching 3 identical symbols on any payline
   - Game ends when balance reaches zero

## Symbols and Payouts

- 🍒 Cherry: 10x bet
- 🍋 Lemon: 20x bet
- 🍊 Orange: 30x bet
- 🍇 Grapes: 40x bet
- 💎 Diamond: 100x bet
- 🎰 Jackpot: 200x bet

## Winning Combinations

Match 3 identical symbols on any of these paylines to win:

- Top row (horizontal)
- Middle row (horizontal)
- Bottom row (horizontal)
- Diagonal from top-left to bottom-right
- Diagonal from top-right to bottom-left

Winnings are calculated by multiplying your bet amount with the symbol's payout value.

## Winning Combinations

Match three identical symbols on any of these lines:

- Top row
- Middle row
- Bottom row
- Diagonal (top-left to bottom-right)
- Diagonal (top-right to bottom-left)

## License

This project is released into the public domain. Feel free to use, modify, and distribute the code as you see fit.
