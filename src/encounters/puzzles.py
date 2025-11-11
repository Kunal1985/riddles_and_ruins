from utils.constants import PUZZLES_DICTIONARY

class Puzzles:
    def __init__(self, player, enemy):
        self.puzzles = PUZZLES_DICTIONARY
        self.player = player
        self.enemy = enemy

    def present_puzzle(self, puzzle_type):
        print("Solve this puzzle to proceed:")
        if puzzle_type in self.puzzles:
            puzzle = self.puzzles[puzzle_type]
            print(puzzle["question"])
            user_answer = input("Your answer (Enter '0' to skip and incur 20 health points): ")
            return self.check_answer(puzzle_type, user_answer)
        else:
            print("Puzzle type not found.")
            return False

    def check_answer(self, puzzle_type, user_answer):
        correct_answer = self.puzzles[puzzle_type]["answer"]
        if user_answer.lower() == correct_answer.lower():
            print("Correct! You've solved the puzzle.")
            self.player.add_item("Health Potion")
            return True
        elif user_answer == '0':
            print("You chose to skip the puzzle and incur a penalty of 20 health points.")
            self.player.take_damage(20)
            return True
        else:
            print(f"Wrong answer. Run away before {self.enemy} is back on the feet. Come back later to try again!.")
            return False