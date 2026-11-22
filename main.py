"""Terminal-based Rock-Paper-Scissors simulator.

A clean, PEP 8-compliant beginner project for GitHub portfolio.
"""

import random

# Immutable tuple of valid options
VALID_CHOICES: tuple[str, ...] = ("rock", "paper", "scissors")


def get_computer_choice() -> str:
    """Randomly selects one option for the computer.

    Returns:
        str: The computer's choice ('rock', 'paper', or 'scissors').
    """
    return random.choice(VALID_CHOICES)


def determine_winner(user_choice: str, computer_choice: str) -> str:
    """Determines the winner based on standard Rock-Paper-Scissors rules.

    Args:
        user_choice (str): The option selected by the user.
        computer_choice (str): The option selected by the computer.

    Returns:
        str: Outcome of the match ('draw', 'win', or 'lose').
    """
    if user_choice == computer_choice:
        return "draw"

    # Set of winning combinations for the user (O(1) lookup time)
    win_cases = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }

    if (user_choice, computer_choice) in win_cases:
        return "win"

    return "lose"


def main() -> None:
    """Main control function for running the game loop."""
    print("=" * 45)
    print("🎮 WELCOME TO ROCK-PAPER-SCISSORS 🎮")
    print("=" * 45)
    print("Rules: Type 'rock', 'paper', or 'scissors'. Type 'exit' to quit.\n")

    user_score = 0
    computer_score = 0
    draw_count = 0

    while True:
        # Sanitize input: strip whitespace and convert to lowercase
        raw_input = input("Enter your choice: ").strip().lower()

        # Handle exit request
        if raw_input in ("exit", "quit", "stop"):
            print("\n" + "=" * 45)
            print("Thanks for playing!")
            print(
                f"🏆 Final Score: You {user_score} - {computer_score} Computer "
                f"(Draws: {draw_count})"
            )
            print("=" * 45)
            break

        # Input validation
        if raw_input not in VALID_CHOICES:
            print("❌ Invalid choice! Please enter 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        result = determine_winner(raw_input, computer_choice)

        if result == "draw":
            draw_count += 1
            print("🤝 It's a tie!\n")
        elif result == "win":
            user_score += 1
            print("🎉 You win this round!\n")
        else:
            computer_score += 1
            print("💻 Computer wins this round!\n")


if __name__ == "__main__":
    main()
