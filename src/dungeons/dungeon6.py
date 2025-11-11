from dungeons.dungeon import Dungeon
from encounters.combat import Combat
from quest import Quest

class Dungeon6(Dungeon):
    def __init__(self, player):
        enemy_name = "Chimeros - the lurking terror of many forms"
        super().__init__(
            "Dungeon 6",
            f"This is last hurdle in your quest for glory, pride & honor. {enemy_name} is not going to make it easy",
            enemy_name,
            player,
            Quest("Quest_Dungeon1", ["riddle6", "combat-3", "riddle2", "combat-4", "math6", "combat-5"])
        )

    def explore(self):
        self.player.current_dungeon = 5
        print(self.description)
        
        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()