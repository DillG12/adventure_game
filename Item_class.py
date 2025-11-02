


class Item:
    def __init__(self, name, description, item_type = "generic", value = 0, rarity = "common", uses = 1):
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
            "common": 20,
            "uncommon": 15,
            "rare": 5,
            "epic": 2,
            "legendary": 1
        }
        return rarity_levels.get(self.rarity.lower(), 1)
    



small_potion = Item(
    "Minor Healing Potion",
    "A small vial filled with red liquid",
    "potion",
    15, #Healing value
    "common"
)

medium_potion = Item(
    "Greater Healing Potion",
    "A regular vial filled with a bright red liquid",
    "potion",
    30,
    "uncommon"
)

large_potion = Item(
    "Superior Healing Potion",
    "A large vial filled with a glowing red liquid",
    "potion",
    50,
    "rare"
)

very_large_potion = Item(
    "Ultimate Healing Potion",
    "A massive vial filled with a radiant red liquid",
    "potion",
    100,
    "epic"
)

special_potion = Item(
    "Elixir of Life",
    "A mystical potion that fully restores health",
    "potion",
    9999,  # Effectively full heal
    "legendary"
)   

short_sword = Item(
    "Short Sword",
    "A basic short sword with a steel blade and a simple hilt",
    "weapon",
    10,
    "common",
    10
)

long_sword = Item(
    "Long Sword",
    "A finely crafted long sword with a sharp steel blade and an ornate hilt",
    "weapon",
    25,
    "uncommon",
    15
)

great_sword = Item(
    "Great Sword",
    "A massive great sword with a heavy steel blade and an intricate hilt",
    "weapon",
    40,
    "rare",
    20
)

enchanted_dagger = Item(
    "Enchanted Dagger",
    "A small dagger that glows with a faint blue light",
    "weapon",
    35,
    "epic",
    25
)

enchanted_staff = Item(
    "Enchanted Staff",
    "A wooden staff topped with a glowing crystal",
    "weapon",
    50,
    "legendary",
    30
)

dice = Item(
    "Mystic Dice",
    "A pair of ancient dice that seem to shimmer with a strange energy",
    10,
    "common"
    )

compass = Item(
    "Brass Compass",
    "A compass that points North",
    15,
    "common"
    )

mirror = Item(
    "Silver Mirror",
    "A hand mirror with an ornate silver frame",
    20,
    "common"
    )

ancient_key = Item(
    "Ancient Key",
    "A rusted key that looks very old",
    25,
    "common"
    )

lantern = Item(
    "Oil Lantern",
    "A lantern that provides light in dark places",
    30,
    "common"
    )

small_pin = Item(
    "Small Pin",
    "A small decorative pin, possibly valuable",
    5,
    "common"
    )

def item_list():
    return [small_potion, medium_potion, large_potion, very_large_potion, special_potion,
            short_sword, long_sword, great_sword, enchanted_dagger, enchanted_staff,
            dice, compass, mirror, ancient_key,
            lantern, small_pin]

