import random
from Item_class import *



class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def is_alive(self):
        return self.health > 0
    
class Player(Character):
    def __init__(self, name, health, attack, inventory_limit = 20, inventory = {}, weapon = None, gold = 0, experience = 0, level = 1, xp_to_next_level = 100):
        super().__init__(name, health, attack)
        self.max_health = health
        self.inventory_limit = inventory_limit
        self.inventory = inventory
        self.weapon = weapon
        self.gold = gold
        self.experience = experience
        self.xp_to_next_level = xp_to_next_level
        self.level = level

    def level_up(self):
        if self.experience >= self.xp_to_next_level:
            self.level += 1
            self.experience -= self.xp_to_next_level
            self.xp_to_next_level += 50
            self.max_health = int(self.max_health * 1.1)
            self.health = self.max_health
            self.attack = int(self.attack * 1.1)
            print(f"Congratulations! {self.name} has leveled up! Health is now {self.max_health} and attack is now {self.attack}.")

    def heal(self, heal_amount):
        if self.health >= self.max_health:
            print("You are already at max health!")
        else:
            health_healed = min(heal_amount, self.max_health - self.health)
            self.health += health_healed
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"You healed for {health_healed} health. Your health is now {self.health}/{self.max_health}")

    def add_item(self, item, quantity=1):
        item_count = sum(self.inventory.values())
        slots_needed = quantity
        if item_count + slots_needed <= self.inventory_limit:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"You picked up {quantity} x {item}")
            return True
        else:
            inventory_space = self.inventory_limit - item_count
            print(f"Cannot pick up {item}! You have {inventory_space} slots left.")
            return False
        
    def display_stats(self):
        print(f"{self.name} currently has {self.health}/{self.max_health} HP")
        print(f"Attack: {self.attack}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}/{self.xp_to_next_level}")
        
    def display_inventory(self):
        print(f"\n{self.name}'s inventory")
        for item, quantity in self.inventory.items():
            print(f"{item.name}: {quantity}")
        print(f"Gold: {self.gold}\n")
        
    def use_item(self):
        self.display_inventory()
        item_choice = input("Which item would you like to use? ")
        if item_choice.lower() == "exit":
            print("Exiting item menu.")
            return
        item_obj_to_use = None
        for item in self.inventory:
            if item.name.lower() == item_choice.lower():
                item_obj_to_use = item
                break

        if item_obj_to_use and self.inventory[item_obj_to_use] > 0:
            if item_obj_to_use.item_type == "potion":
                heal_amount = item_obj_to_use.value
                self.heal(heal_amount)

                self.inventory[item_obj_to_use] -= 1
                if self.inventory[item_obj_to_use] == 0:
                    print(f"You have no more {item_obj_to_use.name}s left.")
                    del self.inventory[item_obj_to_use]
                else:    
                    print(f"You used a {item_obj_to_use.name}. You now have {self.inventory[item_obj_to_use]} {item_obj_to_use.name}s left.")

            if item_obj_to_use.item_type == "weapon":
                if self.inventory[item_obj_to_use] < 1:
                    print(f"You do not have a {item_obj_to_use.name} to equip.")
                    return
                if self.weapon:
                    self.attack -= self.weapon.value
                    print(f"You replaced your {self.weapon.name} with {item_obj_to_use.name}.")
                else:
                    print(f"You equipped {item_obj_to_use.name} as your weapon.")
                self.weapon = item_obj_to_use
                self.attack += item_obj_to_use.value
        
    
                

    def choose_action(self):
        return input("What would you like to do? You can attack or attempt to flee:")
    
class Enemy(Character):
    def __init__(self, name, health, attack, gold_reward = 0, xp_reward = 0, player_level = 1, chance_to_appear = 1):
        super().__init__(name, health, attack)
        self.gold_reward = gold_reward
        self.xp_reward = xp_reward
        self.player_level = player_level
        self.chance_to_appear = chance_to_appear

    def get_scaled_stats(self):
        self.health += (self.player_level - 1) * 10
        self.attack += (self.player_level - 1) * 2
        self.gold_reward += (self.player_level - 1) * 5
        self.xp_reward += (self.player_level - 1) * 10

    def choose_action(self):
        return "attack"
    

def battle(player, enemy,):
    print(f"A vicious {enemy.name} has appeared!")

    while player.is_alive() and enemy.is_alive():
        player_action = player.choose_action()
        if player_action == "attack":
            hit = random.randint(1, 5)
            if hit in range(2, 6):
                critical = random.randint(1, 20)
                if critical == 20:
                    damage = random.randint(player.attack - 5, player.attack + 5) * 2
                    enemy.take_damage(damage)
                    print(f"Critical hit! {player.name} attacks {enemy.name} for {damage} damage!")
                else:
                    damage = random.randint(player.attack - 5, player.attack + 5)
                    enemy.take_damage(damage)
                    print(f"{player.name} attacks {enemy.name} for {damage} damage!")
                if player.weapon:
                    player.weapon.uses -= 1
                    if player.weapon.uses <= 0:
                        print(f"Your {player.weapon.name} has broken!")
                        player.attack -= player.weapon.value
                        del player.inventory[player.weapon]
                        player.weapon = None
            else:
                print(f"{player.name} misses!")  

        elif player_action == "flee":
            success = random.randint(1, 6)
            if success in range(5, 7):
                print("You have successfully escaped!")
                return True
            else:
                print("You could not escape!")

        elif player_action == "inventory":
            if sum(player.inventory.values()) > 0:
                player.use_item()
            else:
                print("You have no items to use!")

        else:
            print("Invalid choice. Please try again.")
            continue

        if not enemy.is_alive():
            print(f"{enemy.name} is defeated!")
            player.gold += enemy.gold_reward
            player.experience += enemy.xp_reward
            print(f"You earned {enemy.xp_reward} experience points!")
            player.level_up()
            print(f"You earned {enemy.gold_reward} gold! You now have {player.gold} gold.")
            return False

        enemy_action = enemy.choose_action()
        if enemy_action == "attack":
            hit = random.randint(1, 5)
            if hit in range(3, 6):
                critical = random.randint(1, 20)
                if critical == 20:
                    damage = random.randint(enemy.attack - 3, enemy.attack + 3) * 2
                    player.take_damage(damage)
                    print(f"Critical hit! {enemy.name} attacks {player.name} for {damage} damage!")
                else:
                    damage = random.randint(enemy.attack - 3, enemy.attack + 3)
                    player.take_damage(damage)
                    print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            else:
                print(f"{enemy.name} misses!")

            if not player.is_alive():
                print(f"{player.name} has been defeated!")
                break
        
        print(f"{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")

ENEMY_TEMPLATES = [
    {"name": "Goblin", "max_hp": 30, "attack_power": 10, "gold_reward": 5, "xp_reward": 20, "chance_to_appear": 50},
    {"name": "Skeleton", "max_hp": 40, "attack_power": 12, "gold_reward": 8, "xp_reward": 30, "chance_to_appear": 40},
    {"name": "Orc", "max_hp": 50, "attack_power": 15, "gold_reward": 12, "xp_reward": 40, "chance_to_appear": 30},
    {"name": "Troll", "max_hp": 60, "attack_power": 18, "gold_reward": 20, "xp_reward": 50, "chance_to_appear": 20},
    {"name": "Dark Knight", "max_hp": 80, "attack_power": 20, "gold_reward": 50, "xp_reward": 100, "chance_to_appear": 10},
    {"name": "Dragon", "max_hp": 100, "attack_power": 25, "gold_reward": 100, "xp_reward": 200, "chance_to_appear": 5},
    {"name": "Demon", "max_hp": 120, "attack_power": 30, "gold_reward": 150, "xp_reward": 300, "chance_to_appear": 1}
]

def get_random_enemy(player):
    player_level = player.level
    enemy_data = random.choices(ENEMY_TEMPLATES, weights=[et["chance_to_appear"] for et in ENEMY_TEMPLATES], k=1)[0]
    enemy = Enemy(
        name=enemy_data["name"],
        health=enemy_data["max_hp"],
        attack=enemy_data["attack_power"],
        gold_reward=enemy_data["gold_reward"],
        xp_reward=enemy_data["xp_reward"],
        player_level=player_level,
        chance_to_appear=enemy_data["chance_to_appear"]
    )
    enemy.get_scaled_stats()
    return enemy
short_sword = Item(
    "Basic Short Sword",
    "A basic short sword with a steel blade and a simple hilt.",
    "weapon",
    10,
    "common",
    1
)
# Example usage
"""player = Player("Hero", 100, 10)
player.add_item(short_sword)
player.use_item()
enemy = Enemy("Goblin", 30, 5)
battle(player, enemy)"""

