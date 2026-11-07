import random
enemies = {"Wasp":45,"Pirate":60,"Kitsune":75}
enemy_names = ["Wasp","Pirate","Kitsune"]
player_health = 100
enemy_health = 0
enemy = ""
def get_enemy(enemy_health,enemy):
    enemy = random.choice(enemy_names)
    enemy_health = enemies[enemy]
    print(f"You are fighting {enemy} with {enemy_health} health.")
    return enemy,enemy_health

def punch(enemy_health):
    damage = random.randint(10,15)
    enemy_health -= damage
    print(f"You punched {enemy} and dealt {damage} damage. {enemy} has {max(0,enemy_health)} health left.")
    return enemy_health

def wasp_attack(player_health):
    damage = random.randint(7,9)
    player_health -= damage
    print(f"Wasp stung you and dealt {damage} damage. You have {max(0,player_health)} health.")
    return player_health

def pirate_attack(player_health):
    damage = random.randint(9,13)
    player_health -= damage
    print(f"Pirate has stabbed you and dealt {damage} damage. You have {max(0,player_health)} health left.")
    return player_health

def kitsune_attack(player_health):
    damage = random.randint(11,23)
    if damage <= 15:
        player_health -= damage
        print(f"Kitsune has mauled you and dealt {damage} damage. You have {max(0,player_health)} health left.")
        return player_health
    if damage >= 16:
        player_health -= damage
        print(f"Critical hit! Kitsune has gutted you and dealt {damage} damage. You have {max(0,player_health)} health left.")
        return player_health

while True:
    if player_health <= 0:
        print(f"You have been defeated by {enemy}.")
        break
    if enemy_health <= 0:
        command = input("Type spawn to fight an enemy: ")
        if command == "spawn":
            enemy,enemy_health = get_enemy(enemy_health,enemy)
        else:
            print("Invalid command.")
    if enemy_health > 0:
        command = input(f"You have {player_health} health. Type punch to attack the {enemy}: ")
        if command == "punch":
            enemy_health = punch(enemy_health)
            if enemy_health <= 0:
                print(f"You have defeated {enemy}.")
            if enemy_health > 0:
                if enemy == "Wasp":
                    player_health = wasp_attack(player_health)
                elif enemy == "Pirate":
                    player_health = pirate_attack(player_health)
                elif enemy == "Kitsune":
                    player_health = kitsune_attack(player_health)
        else:
            print("Invalid command.")
