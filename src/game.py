import random
from player import Player
from dungeons.dungeon1 import Dungeon1
from dungeons.dungeon2 import Dungeon2
from dungeons.dungeon3 import Dungeon3
from dungeons.dungeon4 import Dungeon4
from dungeons.dungeon5 import Dungeon5
from dungeons.dungeon6 import Dungeon6

class Game:
    def __init__(self, player=None):
        self.player = player
        self.is_running = True
        self.locations = [Dungeon1(player), Dungeon2(player), Dungeon3(player), Dungeon4(player), Dungeon5(player), Dungeon6(player)]

    def start_game(self):
        if self.player is None:
            print("Welcome to the Adventure Game!")
            self.player = self.create_player()
            
        # self.prepare_dungeons_with_puzzles()    
        
        self.main_game_loop()
        
    def prepare_dungeons_with_puzzles(self):
        # Create pools of available puzzles
        riddle_pool = [f"riddle{i}" for i in range(1, 7)]  # riddle1 to riddle6
        math_pool = [f"math{i}" for i in range(1, 7)]      # math1 to math6
        
        # Distribute puzzles to dungeons
        dungeon_puzzle_requirements = [
            {"riddles": 1, "math": 0},  # Dungeon 1: 1 riddle
            {"riddles": 1, "math": 0},  # Dungeon 2: 1 riddle
            {"riddles": 0, "math": 1},  # Dungeon 3: 1 math
            {"riddles": 0, "math": 2},  # Dungeon 4: 2 math
            {"riddles": 1, "math": 1},  # Dungeon 5: 1 riddle, 1 math
            {"riddles": 2, "math": 1}   # Dungeon 6: 2 riddles, 1 math
        ]
        
        # Assign random puzzles to each dungeon
        for dungeon, requirements in zip(self.locations, dungeon_puzzle_requirements):
            riddles = random.sample(riddle_pool, requirements["riddles"])
            math = random.sample(math_pool, requirements["math"])
            
            # Remove used puzzles from pools
            for r in riddles:
                riddle_pool.remove(r)
            for m in math:
                math_pool.remove(m)
                
            # Create new quest objectives combining combat and puzzles
            puzzles = riddles + math
            combat = [obj for obj in dungeon.quest.objectives if obj.startswith("combat")]
            new_objectives = combat + puzzles
            
            # Update dungeon's quest objectives
            dungeon.quest.objectives = new_objectives

    def create_player(self, player_name):
        return Player(player_name)

    def main_game_loop(self):
        while self.is_running:
            self.show_menu()
            choice = input("Choose an action: ")
            self.handle_choice(choice)

    def show_menu(self):
        print("\n1. Explore")
        print("2. Check Inventory")
        print("3. Check Player Status")
        print("4. Quit")

    def print_player_status(self):
        print(self.player)
        dungeons_completed = self.player.dungeons_completed
        if not len(dungeons_completed):
            print("You have not completed any dungeons yet.")
            return
        print("You have completed the following dungeons:")
        for dungeon in self.player.dungeons_completed:
            current_dungeon = self.locations[dungeon]
            print(current_dungeon)
            current_dungeon.quest.display_quest_info()

    def handle_choice(self, choice):
        if choice == '1':
            self.explore()
        elif choice == '2':
            self.player.show_inventory()
        elif choice == '3':
            self.print_player_status()
        elif choice == '4':
            self.is_running = False
            print("Thanks for playing!")
        else:
            print("Invalid choice. Please try again.")

    def reset_game(self):
        choice = input("Do you want to play from the start (yes/no): ")
        if choice.lower() == 'yes':
            self.player = self.create_player(self.player.name)
        else:
            return    

    def explore(self):
        print("You venture into the unknown...")
        if not self.player:
            print("No player found. Create a player first.")
            return
        next_dungeons = self.player.next_dungeons
        # Proceed based on available dungeons
        if len(next_dungeons) >= 1:
            # Check if player is alive
            if not self.player.is_alive():
                print("Sorry, you don't have enough health points. GAME OVER!!!")
                self.reset_game()
                return
            # Both paths available
            if len(next_dungeons) > 1:
                num1, num2 = next_dungeons
                print(f"You have two paths ahead: (1) Dungeon {num1 + 1} or (2) Dungeon {num2 + 1}")
                choice = input("Select the dungeon you want to explore: ")
                if choice == '1':
                    selected_dungeon = self.locations[num1]
                elif choice == '2':
                    selected_dungeon = self.locations[num2]
                else:
                    print("Invalid choice. Returning to main menu.")
                    return
                selected_dungeon.explore()
            # Single path available    
            else:
                current_dungeon = next_dungeons[0]
                print(f"You proceed to Dungeon {current_dungeon + 1}.")
                self.locations[current_dungeon].explore()
        # All dungeons explored!
        else:
            print("All stages completed!")
            self.reset_game()
