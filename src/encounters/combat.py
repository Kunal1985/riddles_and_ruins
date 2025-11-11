import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self, penalty_health):
        battle_result = random.choice([0, 1])
        final_damage = penalty_health/2
        stage_clear = False
        if battle_result == 1:
            final_damage = penalty_health/4
            print(f"You defeated the {self.enemy}! You lost {final_damage} health points in the battle.")
            self.player.add_item("Battle Potion")
            stage_clear = True
        else:
            print(f"You were defeated by the {self.enemy} and lost {final_damage} health points.")
        if self.player.battle_potions_in_use:    
            print("Your Battle Potion protected you from extra damage!")
        else:
            self.player.take_damage(final_damage)
        self.player.battle_potions_in_use = False    
        return stage_clear    

    def skip(self, penalty_health):
        print(f"You were afraid to fight the {self.enemy} and are penalized {penalty_health} health points.")
        if not self.player.battle_potions_in_use:
            self.player.take_damage(penalty_health)
        else:
            print("Your Battle Potion protected you from extra damage!")
        self.player.battle_potions_in_use = False    
        return True    

    def decide(self, penalty_health):
        action = input(f"Choose your action: (1) Fight (2) Skip [you will lose {penalty_health} health points]: ")
        match action:
            case '1':
                print("You brace yourself for the enemy's attack.")
                return self.fight(penalty_health)
            case '2':
                return self.skip(penalty_health)
            case _:
                print("Invalid action. Try again.")
                return False