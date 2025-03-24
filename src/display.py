"""Display module for the CLI slots game.

This module handles the visual presentation of the slot machine including:
- Rendering the slot machine interface
- Displaying spinning animations
- Showing game status and messages
"""

import os
import time
from typing import List, Tuple

from .config import VISIBLE_ROWS


def clear_screen():
    """Clear the terminal screen and reset cursor position."""
    if os.name == 'nt':
        os.system('cls')
    else:
        # ANSI escape codes for complete screen clearing and cursor reset
        print('\033[2J\033[H', end='')


def create_reel_frame(reels: List[List[str]], highlight_positions: List[Tuple[int, int]] = None) -> str:
    """Create a frame of the slot machine display.
    
    Args:
        reels: The current state of all reels
        highlight_positions: Optional list of (x, y) positions to highlight (for winning lines)
    
    Returns:
        A string containing the slot machine display
    """
    highlight_positions = highlight_positions or []
    
    # Create the frame content
    frame_lines = []
    
    # Create the top border
    frame_lines.append('+------+------+------+')
    
    # Create the reel display
    for row in range(VISIBLE_ROWS):
        line = '|'
        for col, reel in enumerate(reels):
            symbol = reel[row]
            # Center the symbol in a fixed-width cell
            if (col, row) in highlight_positions:
                line += f' *{symbol}* '
            else:
                line += f'  {symbol}  '
            if col < len(reels)-1:
                line += '|'
        line += '|'
        frame_lines.append(line)
    
    # Create the bottom border
    frame_lines.append('+------+------+------+')
    
    return '\n'.join(frame_lines)


def animate_spin(reels: List[List[str]], frames: int = 10, delay: float = 0.1) -> None:
    """Create a spinning animation effect.
    
    Args:
        reels: The final state of the reels after spinning
        frames: Number of animation frames
        delay: Delay between frames in seconds
    """
    from .config import SYMBOLS
    symbols = list(SYMBOLS.keys())
    
    # Initial cleanup
    clear_screen()
    time.sleep(0.05)  # Small delay to ensure clean slate
    
    for frame in range(frames):
        # Generate a random frame
        temp_reels = []
        for col in range(len(reels)):
            # Create a column of random symbols
            temp_symbols = [symbols[(frame + col + row) % len(symbols)] for row in range(VISIBLE_ROWS)]
            temp_reels.append(temp_symbols)
        
        # Clear and display with proper timing
        clear_screen()
        print(create_reel_frame(temp_reels))
        time.sleep(delay)
    
    # Ensure clean final state display
    clear_screen()
    time.sleep(0.05)  # Small delay for clean transition
    print(create_reel_frame(reels))