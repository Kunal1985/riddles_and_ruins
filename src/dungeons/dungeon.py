from encounters.combat import Combat
from encounters.puzzles import Puzzles
from utils.constants import COMBAT_PENALTY_POINTS

class Dungeon:
    def __init__(self, name, description, enemy, player, quest):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.player = player
        self.quest = quest

    def __str__(self):
        return f"{self.name}: {self.description}."
    
    def complete_objectives(self):
        while len(self.quest.objectives):
            objective = self.quest.objectives[0]
            objective_completed = False
            if "combat" in objective:
                objective_completed = self.engage_combat(objective)
            else:
                objective_completed = self.solve_puzzle(objective)
            
            # Mark objective as complete
            if objective_completed:        
                self.quest.complete_objective(objective)
            else:
                print(f"You failed to complete the objective: {objective}")
                break  # Stop further attempts if one objective fails
    
    def mark_stage_complete(self):
        if self.quest.is_completed():
            self.player.stage_complete()
    
    def engage_combat(self, combat_type):
        combat_level = combat_type and int(combat_type.split("-")[1]) or 1
        if combat_level > 3:
            combat_level = 3  # Cap combat level to 3
        combat = Combat(self.player, self.enemy)
        final_penalty_points = COMBAT_PENALTY_POINTS[combat_level]
        return combat.decide(final_penalty_points)
    
    def solve_puzzle(self, puzzle_type):
        return Puzzles(self.player, self.enemy).present_puzzle(puzzle_type)