import random

class LotteryGame:
    def __init__(self):
        self.winning_numbers = self.generate_winning_numbers()

    def generate_winning_numbers(self):
        """Randomly generate 6 unique numbers from 1–60."""
        return sorted(random.sample(range(1, 61), 6))

    def check_matches(self, player_numbers):
        """Return how many numbers the player got right."""
        return len(set(self.winning_numbers) & set(player_numbers))

    def calculate_prize(self, matches):
        """Compute the total prize based on matches."""
        if matches == 6:
            return 1_000_000  # Jackpot
        else:
            return matches * 1_000  # ₱1,000 per match

    def display_results(self, player_numbers):
        """Show all results: winning numbers, player numbers, matches, prize."""
        matches = self.check_matches(player_numbers)
        prize = self.calculate_prize(matches)

        print("\n--- LOTTERY RESULTS ---")
        print(f"Winning Numbers: {self.winning_numbers}")
        print(f"Your Numbers:    {sorted(player_numbers)}")
        print(f"Matched Numbers: {matches}")
        print(f"Prize: ₱{prize:,.0f}")
        print("-----------------------")


class Player:
    def __init__(self, name):
        self.name = name
        self.numbers = []

    def choose_numbers(self):
        """Allow player to input 6 numbers between 1–60."""
        print(f"\nHello {self.name}, enter your 6 chosen numbers (1–60):")
        while len(self.numbers) < 6:
            try:
                num = int(input(f"Enter number {len(self.numbers) + 1}: "))
                if num < 1 or num > 60:
                    print("❌ Number must be between 1 and 60.")
                elif num in self.numbers:
                    print("❌ Number already chosen.")
                else:
                    self.numbers.append(num)
            except ValueError:
                print("❌ Please enter a valid number.")
        self.numbers.sort()


# ---------- MAIN PROGRAM ----------
def main():
    game = LotteryGame()
    player = Player("Player 1")
    player.choose_numbers()
    game.display_results(player.numbers)


if __name__ == "__main__":
    main()
