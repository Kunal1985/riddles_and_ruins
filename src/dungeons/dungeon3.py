from dungeons.dungeon import Dungeon
from quest import Quest

class Dungeon3(Dungeon):
    def __init__(self, player):
        enemy_name = "Viperion - the massive serpent"
        super().__init__(
            "Dungeon 3",
            f"Crawl into the foggy damp tunnel. A hissing sounds is reaching you from the mist. {enemy_name} is ready to strike",
            enemy_name,
            player,
            Quest("Quest_Dungeon1", ["math2", "combat-1"])
        )

    def explore(self):
        self.player.current_dungeon = 2
        print(self.description)
        
        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()