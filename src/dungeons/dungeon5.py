from dungeons.dungeon import Dungeon
from quest import Quest

class Dungeon5(Dungeon):
    def __init__(self, player):
        enemy_name = "BoneDragon - the undead wyrm"
        super().__init__(
            "Dungeon 5",
            f"Hide or face your destiny in this dungeon of death. {enemy_name} is hungry for souls",
            enemy_name,
            player,
            Quest("Quest_Dungeon1", ["combat-2", "riddle3", "math5"])
        )

    def explore(self):
        self.player.current_dungeon = 4
        print(self.description)

        # Complete objectives
        self.complete_objectives()

        # Check if all objectives met    
        self.mark_stage_complete()