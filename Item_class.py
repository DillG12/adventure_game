


class Item:
    def __init__(self, name, description, item_type = "generic", value = 0):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.value = value

    def __str__(self):
        return self.name
    



small_potion = Item(
    "Minor Healing Potion",
    "A small vial filled with red liquid",
    "potion",
    15 #Healing value
)

medium_potion = Item(
    "Greater Healing Potion",
    "A regular vial filled with a bright red liquid",
    "potion",
    30
)

large_potion = Item(
    "Superior Healing Potion",
    "A large vial filled with a glowing red liquid",
    "potion",
    50 
)

short_sword = Item(
    "Short Sword",
    "A basic short sword with a steel blade and a simple hilt",
    "weapon",
    10
)

long_sword = Item(
    "Long Sword",
    "A finely crafted long sword with a sharp steel blade and an ornate hilt",
    "weapon",
    25
)

great_sword = Item(
    "Great Sword",
    "A massive great sword with a heavy steel blade and an intricate hilt",
    "weapon",
    40 #Attack value
)

dice = Item(
    "Mystic Dice",
    "A pair of ancient dice that seem to shimmer with a strange energy",
    10 #Gold value
    )

compass = Item(
    "Brass Compass",
    "A compass that points North",
    15 #Gold value
    )

mirror = Item(
    "Silver Mirror",
    "A hand mirror with an ornate silver frame",
    20 #Gold value
    )

ancient_key = Item(
    "Ancient Key",
    "A rusted key that looks very old",
    25 #Gold value
    )

lantern = Item(
    "Oil Lantern",
    "A lantern that provides light in dark places",
    30 #Gold value
    )

small_pin = Item(
    "Small Pin",
    "A small decorative pin, possibly valuable",
    5 #Gold value
    )

def item_list():
    return [small_potion, medium_potion, large_potion,
            short_sword, long_sword, great_sword,
            dice, compass, mirror, ancient_key,
            lantern, small_pin]

