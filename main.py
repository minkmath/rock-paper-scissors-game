"""Terminal-based Rock-Paper-Scissors game with Best-of-3 mode.

A clean, PEP 8-compliant beginner project for GitHub portfolio.
"""

import random

# Immutable tuple of valid options
VALID_CHOICES: tuple[str, ...] = ("rock", "paper", "scissors")
TARGET_SCORE: int = 2  # First to 2 wins takes the match (Best of 3)


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


def calculate_win_rate(user_score: int, total_rounds: int) -> float:
    """Calculates the user's win rate percentage.

    Args:
        user_score (int): Number of rounds won by user.
        total_rounds (int): Total played rounds including draws.

    Returns:
        float: Win rate percentage rounded to 1 decimal place.
    """
    if total_rounds == 0:
        return 0.0
    return round((user_score / total_rounds) * 100, 1)


def main() -> None:
    """Main control function for running the Best-of-3 game loop."""
    print("=" * 50)
    print("🎮 WELCOME TO ROCK-PAPER-SCISSORS (BEST OF 3) 🎮")
    print("=" * 50)
    print(f"Rules: First to reach {TARGET_SCORE} wins takes the match!")
    print("Options: Type 'rock', 'paper', or 'scissors'. Type 'exit' to quit.\n")

    user_score = 0
    computer_score = 0
    draw_count = 0
    round_number = 1

    while True:
        print(f"--- Round {round_number} ---")
        print(f"Scoreboard: You {user_score} - {computer_score} Computer")
        raw_input = input("Enter your choice: ").strip().lower()

        # Handle exit request
        if raw_input in ("exit", "quit", "stop"):
            print("\nGame exited by player.")
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
            print("🎉 You won this round!\n")
        else:
            computer_score += 1
            print("💻 Computer won this round!\n")

        round_number += 1

        # Check Best-of-3 Match Winner Condition
        if user_score == TARGET_SCORE or computer_score == TARGET_SCORE:
            print("=" * 50)
            if user_score == TARGET_SCORE:
                print("🏆 CONGRATULATIONS! YOU WON THE MATCH! 🏆")
            else:
                print("💻 GAME OVER! COMPUTER WON THE MATCH! 💻")

            total_rounds = user_score + computer_score + draw_count
            win_rate = calculate_win_rate(user_score, total_rounds)

            print(
                f"Match Summary: You {user_score} - {computer_score} Computer "
                f"(Draws: {draw_count})"
            )
            print(f"Total Rounds Played: {total_rounds}")
            print(f"Your Win Rate: {win_rate}%")
            print("=" * 50)
            break


if __name__ == "__main__":
    main()
    
