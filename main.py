import random
from Item_class import *
from character_class import Player, battle
from room_class import Room, ROOM_NAMES, random_room


def main():
    print("Welcome to the Adventure Game!")
    print("1. Start New Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
        
    if choice == '1':
        player_name = input("Enter your character's name: ")
        player = Player(name=player_name, health=100, attack=10)
        print(f"Character {player.name} created with {player.health} health and {player.attack} attack.")
        game_loop = True
    elif choice == '2':
        print("Exiting the game. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")


    while game_loop:
        current_room = random_room(player)
        print(f"You have entered the {current_room.name}: {current_room.description}")

        if current_room.enemies:
            for enemy in current_room.enemies:
                battle(player, enemy)
            if not player.is_alive():
                print("You have been defeated. Game Over.")
                break
            print("You have emerged victorious!\n The room is now safe.")
            safe = True
        else:
            print("The room is peaceful. You can explore safely.")
            safe = True
        while safe and player.is_alive():
            if current_room.visible_items:
                print("You see the following items:")
                for item in current_room.visible_items:
                    print(f"- {item.name}: {item.description}")
            else:
                print("There are no visible items in this room.")
            choice = input("What would you like to do? (search/loot/move/inventory/status/exit): ")
            if choice == "search":
                current_room.search_room(player)
            elif choice == "loot":
                if current_room.visible_items:
                    for item in current_room.visible_items:
                        choice = input(f"Do you want to pick up {item.name}? (yes/no): ")
                        if choice.lower() == "yes":
                            player.add_item(item)
                            print(f"You picked up {item.name}.")
                            current_room.visible_items.remove(item)
                        elif choice.lower() == "no":
                            print(f"You left {item.name} behind.")
                            current_room.visible_items.remove(item)
                        else:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
                        if current_room.visible_items == []:
                            print("You have looted all visible items.")
                else:
                    print("There are no items to loot.")
            elif choice == "move":
                print("You move to the next room.")
                safe = False
            elif choice == "inventory":
                player.use_item()
            elif choice == "status":
                player.display_stats()
            elif choice == "exit":
                print("Exiting the game. Goodbye!")
                safe = False
                game_loop = False
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()