from dungeons.dungeon import Dungeon
from quest import Quest

class Dungeon4(Dungeon):
    def __init__(self, player):
        enemy_name = "DarkSorcerer - the master of shadows"
        super().__init__(
            "Dungeon 4",
            f"You enter the pitch dark cave. All of your senses seem like they are off. {enemy_name} hasn't tricked someone in a while",
            enemy_name,
            player,
            Quest("Quest_Dungeon1", ["combat-2", "math3", "math4"])
        )

    def explore(self):
        self.player.current_dungeon = 3
        print(self.description)
        
        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()