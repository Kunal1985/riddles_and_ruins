from player import Player
from game import Game

def main():
    print("Welcome to the Adventure: Riddles & Ruins!")
    player_name = input("Enter your character's name: ")
    
    # Initialize the player
    player = Player(name=player_name)
    
    # Start the game
    game = Game(player)
    game.start_game()

if __name__ == "__main__":
    main()