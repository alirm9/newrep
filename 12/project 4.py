class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Room:
    def __init__(self, name, item=None):
        self.name = name
        self.item = item

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.location = starting_room
        self.inventory = []

    def move(self, new_room):
        self.location = new_room
        print(f"{self.name} moved to {self.location.name}.")

    def collect_item(self):
        if self.location.item:
            collected_item = self.location.item
            self.inventory.append(collected_item)
            print(f"{self.name} picked up: {collected_item.name}.")
            self.location.item = None # Remove item from the room
        else:
            print(f"There is nothing to collect in {self.location.name}.")

# --- Game Initialization ---

# Create items
map_item = Item("Old Map", 0.2)
key_item = Item("Iron Key", 0.5)

# Create rooms
entrance = Room("Entrance Hall")
library = Room("Library", map_item)
dungeon = Room("Dungeon", key_item)

# Create player
player = Player("Explorer", entrance)

# Simulate basic menu actions
player.move(library)
player.collect_item()
player.move(dungeon)
player.collect_item()

print(f"\n{player.name}'s Inventory: {[i.name for i in player.inventory]}")