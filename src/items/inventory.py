class Inventory:
    def __init__(self):
        self.items = {
            "Health Potion": 0,
            "Battle Potion": 0,
        }

    def add_item(self, item_type):
        if item_type in self.items.keys():
            self.items[item_type] += 1
            print(f"One {item_type} added to your inventory. You now have {self.items[item_type]} {item_type}(s).")

    def remove_item(self, item_type):
        if item_type in self.items.keys():
            self.items[item_type] -= 1
        print(f"You use One {item_type} from your inventory. You now have {self.items[item_type]} {item_type}(s).")

    def show_inventory(self):
        print("Your Inventory:")
        index = 0
        # Prepare user prompt
        for (item, quantity) in self.items.items():
            index += 1
            print(f"{index}. {item} (x{quantity})")
        last_index = index + 1    
        print(f"{last_index}. SKIP")
        choice = int(input("Enter the item you want to use: "))
        items_list = list(self.items.keys())

        # Process user choice
        if choice != last_index and 1 <= choice <= len(items_list):
            item_to_use = items_list[choice - 1]
            if self.items[item_to_use] > 0:
                self.exec_use_item(item_to_use)
                return item_to_use    
            else:
                print("You don't have that item or it's out of stock.")

    def exec_use_item(self, item_to_use):
        self.remove_item(item_to_use)
        if item_to_use == "Health Potion":
            print(f"You restored 20 {item_to_use}.")
        elif item_to_use == "Battle Potion":
            print(f"You will not loose any health if you face battle challenge in the next dungeon.")    