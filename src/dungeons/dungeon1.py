from dungeons.dungeon import Dungeon
from quest import Quest

class Dungeon1(Dungeon):
    def __init__(self, player):
        enemy_name = "StoneGiant - the towering rock behemoth"
        super().__init__(
          "Dungeon 1",
          f"Welcome to the mountain of rocks and the deepest valleys. {enemy_name} stands before you.",
          enemy_name,
          player,
          Quest("Quest_Dungeon1", ["riddle1"])
        )

    def explore(self):
        self.player.current_dungeon = 0
        print(self.description)
        
        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()