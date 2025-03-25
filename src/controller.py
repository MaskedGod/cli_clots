"""Game controller module for managing game flow and user interactions.

This module implements the game controller that coordinates between
the slot machine logic and user interface components.
"""

from .game import SlotMachine
from .display import clear_screen, create_reel_frame, animate_spin
from .config import MIN_BET, DEFAULT_BET


class BetManager:
    """Manages betting operations and validation."""

    @staticmethod
    def get_bet(machine: SlotMachine) -> int:
        """Get and validate bet amount from user input.

        Args:
            machine: Current slot machine instance

        Returns:
            Valid bet amount
        """
        while True:
            try:
                bet = int(input(f"Enter bet amount ({MIN_BET}-{machine.balance}): "))
                if MIN_BET <= bet <= machine.balance:
                    return bet
                print(f"Bet must be between {MIN_BET} and {machine.balance}")
            except ValueError:
                print("Please enter a valid number")


class GameController:
    """Controls game flow and user interactions."""

    def __init__(self):
        self.machine = SlotMachine()
        self.bet_manager = BetManager()
        self.bet = DEFAULT_BET

    def _handle_spin(self) -> None:
        """Handle spin action and its results."""
        if self.machine.balance < self.bet:
            print("\nInsufficient balance!")
            input("Press Enter to continue...")
            return

        reels, valid_bet = self.machine.spin(self.bet)
        if not valid_bet:
            print("\nInvalid bet amount!")
            input("Press Enter to continue...")
            return

        animate_spin(reels)

        win_amount, winning_lines = self.machine.check_wins(self.bet)
        if win_amount > 0:
            clear_screen()
            print(f"\nWIN! ${win_amount}")
            print(create_reel_frame(reels, winning_lines[0]))
        else:
            print("\nNo win this time!")

        input("\nPress Enter to continue...")

    def _display_game_state(self) -> None:
        """Display current game state."""
        clear_screen()
        print(f"\nBalance: ${self.machine.balance}")
        print(create_reel_frame(self.machine.reels))

    def run(self) -> None:
        """Main game loop."""
        while True:
            self._display_game_state()

            if self.machine.balance <= 0:
                print("\nGame Over! You're out of money!")
                break

            action = input("\nCommands: [s]pin, [b]et, [q]uit: ").lower()

            if action == "q":
                break
            elif action == "b":
                self.bet = self.bet_manager.get_bet(self.machine)
            elif action == "s":
                self._handle_spin()
