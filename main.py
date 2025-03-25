"""Main entry point for the CLI slots game.

This module initializes and runs the game controller.
"""

from src.controller import GameController


def main():
    """Initialize and run the game."""
    controller = GameController()
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()
