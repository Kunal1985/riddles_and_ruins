from items.inventory import Inventory

path1 = [0, 1, 3, 5]
path2 = [0, 2, 4, 5]
PATHS = [path1, path2]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = Inventory()
        self.current_dungeon = None
        self.next_dungeons = [0]
        self.dungeons_completed = []
        self.battle_potions_in_use = False

    def stage_complete(self):
        stage_completed = self.current_dungeon
        # record completion
        if stage_completed not in self.dungeons_completed:
            self.dungeons_completed.append(stage_completed)

        next_set = set()

        # For each path, the next available stage is the first uncompleted node
        # whose immediate predecessor is completed (or the first node of the path).
        for path in PATHS:
            for i, node in enumerate(path):
                if node in self.dungeons_completed:
                    continue  # already done — keep scanning
                # node is the first uncompleted in this path
                if i == 0:
                    # start of path is always available if not completed
                    next_set.add(node)
                else:
                    prev = path[i - 1]
                    if prev in self.dungeons_completed:
                        next_set.add(node)
                break  # only consider the first uncompleted node on this path

        if not next_set:
            # nothing left on any path
            self.next_dungeons = []
            print("All stages completed!")
        else:
            self.next_dungeons = sorted(next_set)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def add_item(self, item):
        self.inventory.add_item(item)

    def remove_item(self, item):
        self.inventory.remove_item(item)

    def show_inventory(self):
        inventory_used = self.inventory.show_inventory()
        match inventory_used:
            case "Health Potion": self.heal(20)
            case "Battle Potion": self.battle_potions_in_use = True

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Player: {self.name}, Health: {self.health}"