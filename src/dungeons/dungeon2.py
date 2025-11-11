from dungeons.dungeon import Dungeon
from quest import Quest

class Dungeon2(Dungeon):
    def __init__(self, player):
        enemy_name = "FireKnight - the giant armored foe"
        super().__init__(
          "Dungeon 2",
          f"Dare to survive & escape from this hot and steamy cave. {enemy_name} blocks your path.",
          enemy_name,
          player,
          Quest("Quest_Dungeon1", ["combat-1", "riddle2"])
        )

    def explore(self):
        self.player.current_dungeon = 1
        print(self.description)
        
        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()