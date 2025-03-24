from src.game import SlotMachine
from src.display import clear_screen, create_reel_frame, animate_spin
from src.config import MIN_BET, MAX_BET, DEFAULT_BET, INITIAL_BALANCE


def get_bet(machine: SlotMachine) -> int:
    """Get bet amount from user input."""
    while True:
        try:
            bet = int(input(f"Enter bet amount ({MIN_BET}-{machine.balance}): "))
            if MIN_BET <= bet <= machine.balance:
                return bet
            print(f"Bet must be between {MIN_BET} and {machine.balance}")
        except ValueError:
            print("Please enter a valid number")


def main():
    # Initialize game
    machine = SlotMachine()
    bet = DEFAULT_BET

    while True:
        clear_screen()
        if machine.balance <= 0:
            print("\nGame Over! You're out of money!")
            break
            
        print(f"\nBalance: ${machine.balance}")
        print(create_reel_frame(machine.reels))
        
        # Get player action
        action = input("\nCommands: [s]pin, [b]et, [q]uit: ").lower()
        
        if action == 'q':
            break
        elif action == 'b':
            bet = get_bet(machine)
            continue
        elif action == 's':
            if machine.balance < bet:
                print("\nInsufficient balance!")
                input("Press Enter to continue...")
                continue
            
            # Spin the reels
            reels, valid_bet = machine.spin(bet)
            if not valid_bet:
                print("\nInvalid bet amount!")
                input("Press Enter to continue...")
                continue
                
            animate_spin(reels)
            
            # Check for wins
            win_amount, winning_lines = machine.check_wins(bet)
            if win_amount > 0:
                clear_screen()
                print(f"\nWIN! ${win_amount}")
                print(create_reel_frame(reels, winning_lines[0]))
            else:
                print("\nNo win this time!")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThanks for playing!")
