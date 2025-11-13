


class Item:
    def __init__(self, name, description, item_type = "generic", value = 0, rarity = 20, uses = 1):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.value = value
        self.rarity = rarity
        self.uses = uses

    def __str__(self):
        return self.name
    
    def rarity_level(self):
        rarity_levels = {
            50: "common",
            25: "uncommon",
            10: "rare",
            2: "epic",
            1: "legendary"
        }
        return rarity_levels.get(self.rarity.lower(), "unknown")
    



ITEM_TEMPLATES = [
    {"name": "Minor Healing Potion", "description": "A small vial filled with red liquid", "item_type": "potion", "value": 15, "rarity": 50, "uses": 1},

    {"name": "Greater Healing Potion", "description": "A regular vial filled with a bright red liquid", "item_type": "potion", "value": 30, "rarity": 25, "uses": 1},

    {"name": "Superior Healing Potion", "description": "A large vial filled with a glowing red liquid", "item_type": "potion", "value": 50, "rarity": 10, "uses": 1},

    {"name": "Epic Healing Potion", "description": "A massive vial filled with a radiant red liquid", "item_type": "potion", "value": 100, "rarity": 2, "uses": 1},

    {"name": "Elixir of Life", "description": "A mystical potion that fully restores health", "item_type": "potion", "value": 9999, "rarity": 1, "uses": 1},

    {"name": "Short Sword", "description": "A basic short sword with a steel blade and a simple hilt", "item_type": "weapon", "value": 10, "rarity": 50, "uses": 10},

    {"name": "Long Sword", "description": "A finely crafted long sword with a sharp steel blade and an ornate hilt", "item_type": "weapon", "value": 25, "rarity": 25, "uses": 15},

    {"name": "Great Sword", "description": "A massive great sword with a heavy steel blade and an intricate hilt", "item_type": "weapon", "value": 40, "rarity": 10, "uses": 20},

    {"name": "Enchanted Dagger", "description": "A small dagger that glows with a faint blue light", "item_type": "weapon", "value": 35, "rarity": 2, "uses": 25},

    {"name": "Enchanted Staff", "description": "A wooden staff topped with a glowing crystal", "item_type": "weapon", "value": 50, "rarity": 1, "uses": 30},

    {"name": "Mystic Dice", "description": "A pair of ancient dice that seem to shimmer with a strange energy", "item_type": "misc", "value": 10, "rarity": 50, "uses": 1},

    {"name": "Brass Compass", "description": "A compass that points North", "item_type": "misc", "value": 15, "rarity": 50, "uses": 1},

    {"name": "Silver Mirror", "description": "A hand mirror with an ornate silver frame", "item_type": "misc", "value": 20, "rarity": 50, "uses": 1},

    {"name": "Ancient Key", "description": "A rusted key that looks very old", "item_type": "misc", "value": 25, "rarity": 50, "uses": 1},

    {"name": "Oil Lantern", "description": "A lantern that provides light in dark places", "item_type": "misc", "value": 30, "rarity": 50, "uses": 1},

    {"name": "Small Pin", "description": "A small decorative pin, possibly valuable", "item_type": "misc", "value": 5, "rarity": 50, "uses": 1},

    {"name": "Ruby Ring", "description": "A ring set with a large red ruby", "item_type": "misc", "value": 100, "rarity": 25, "uses": 1},

    {"name": "Emerald Necklace", "description": "A necklace adorned with a shining emerald", "item_type": "misc", "value": 150, "rarity": 2, "uses": 1},

    {"name": "Diamond Crown", "description": "A crown encrusted with sparkling diamonds", "item_type": "misc", "value": 500, "rarity": 1, "uses": 1},
]

def generate_item():
    import random

    item_data = random.choices(ITEM_TEMPLATES, weights=[item["rarity"] for item in ITEM_TEMPLATES], k=1)[0]
    item = Item(
        name=item_data["name"],
        description=item_data["description"],
        item_type=item_data["item_type"],
        value=item_data["value"],
        rarity=item_data["rarity"],
        uses=item_data["uses"]
    )


    return item
    

