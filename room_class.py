import random
from Item_class import *
from character_class import ENEMY_TEMPLATES, Enemy, get_random_enemy, Player

class Room:
    def __init__(self, name, description, visible_items=None, hidden_items=None, enemies=None):
        self.name = name
        self.description = description
        self.visible_items = visible_items if visible_items is not None else []
        self.hidden_items = hidden_items if hidden_items is not None else []
        self.enemies = enemies if enemies is not None else []

    def __str__(self):
        output = f"\n--- {self.name} ---\n {self.description}\n\n"

        if self.visible_items:
            output += "You see the following:\n" + ", ".join(self.visible_items) + ".\n"
        else:
            output += "The room appears to be empty.\n"

        if self.exits:
            exit_list = [f"{direction.capitalize()} -> {destination}" for direction, destination in self.exits.items()]
            output += "\nAvailable exits:\n" 
            output += " |".join(exit_list)
        else:
            output += "You are trapped! There are no visible exits."

    def search_room(self, player):
        if not self.hidden_items:
            print("It doesn't appear there are any more items in here.")
            return None
        else:
            found = random.randint(1, 20)
            if found in range(5, 21):
                item_index = random.randint(0, len(self.hidden_items)-1)
                found_item = self.hidden_items.pop(item_index)
                self.visible_items.append(found_item)
                print(f"You found {found_item}!")
                player.experience += 10
                player.level_up()
                return found_item
            else:
                print("You didn't find anything in your search.")
                return None
    
            

ROOM_NAMES = {"The Chamber of Whispers": """A thick, unnatural shade fills this chamber, making the farthest reaches barely visible. 
A faint, constant murmuring sound seems to come from the stone walls themselves, which are covered in faint, glowing runes.
 The air is dead quiet and still, yet filled with the sound of phantom voices.""",

              "The Luminous Grotto": """This cavernous grotto is illuminated by an ethereal, bluish light that seems to emanate from the very walls themselves.
 The walls are covered in bioluminescent moss and fungi, casting an otherworldly glow throughout the space. 
A gentle, cool breeze rustles through the air, carrying with it the faint scent of damp earth and minerals.""",

              "The Obsidian Hall": """This grand hall is constructed entirely of polished black obsidian, which reflects light in a way that creates an almost mirror-like effect.
 The ceiling is high and vaulted, with intricate carvings depicting ancient battles and mythical creatures. 
The air is cool and dry, with a faint echo that amplifies even the slightest sound.""",

              "The Crystal Cavern": """This cavern sparkles with countless crystals jutting out from the walls and ceiling, reflecting light in a dazzling array of colors.
 The floor is uneven and rocky, with small pools of clear water scattered throughout. 
A faint hum can be heard, as if the crystals themselves are resonating with some unseen energy.""",

              "The Forgotten Library": """Dusty shelves line the walls of this ancient library, filled with tomes and scrolls that seem to date back centuries.
 The air is thick with the scent of old paper and leather, and the only light comes from a few flickering candles placed haphazardly around the room."""}

def random_room(player):
    name = random.choice(list(ROOM_NAMES.keys()))
    description = ROOM_NAMES[name]
    room_items = random.choices(item_list(), weights=[item.rarity_level() for item in item_list()], k=random.randint(0, 3))
    enemies = [get_random_enemy(player) for _ in range(random.randint(0, 1))]
    if len(room_items) == 0:
        return Room(name, description, [], [], enemies)
    index = random.randint(0, len(room_items)-1)
    visible_items = room_items[index:]
    hidden_items = room_items[:index]
    return Room(name, description, visible_items, hidden_items, enemies)

    

