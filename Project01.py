print("\nWelcome to Epic Fighting!")
print("You will meet 4 Enemies to meet the Reason of all Disasters 'The DRAGON'")
import random
# PLAYER DATA
player = {
    "name": "Warrior",
    "health": 100,
    "max_health": 100,
    "attack": 20,
    "defense": 10,
    "potions": 3,
    "gold": 0
}
# ENEMIES 
enemies = {
    "Goblin1": {
        "name": "Goblin",
        "health": 50,
        "attack": 10,
        "defense": 5,
        "gold": 30
    },

    "Goblin2": {
        "name": "Goblin",
        "health": 50,
        "attack": 10,
        "defense": 5,
        "gold": 30
    },

    "Orc1": {
        "name": "Orc",
        "health": 80,
        "attack": 18,
        "defense": 8,
        "gold": 40
    },

    "Orc2": {
        "name": "Orc",
        "health": 80,
        "attack": 18,
        "defense": 8,
        "gold": 40
    },

    "Dragon": {
        "name": "Dragon",
        "health": 150,
        "attack": 30,
        "defense": 15,
        "gold": 100
    }
}
game_log = {
    "enemies_killed": 0,
    "potions_used": 0,
    "gold_earned": 0
}

def attack_enemy(attacker, defender):
    roll = random.randint(0, 10)

    if roll < 2:
        print("❌ Attack Missed!")
        return

    damage = attacker["attack"] - defender["defense"] + roll

    if damage < 0:
        damage = 0

    if roll > 8:
        damage *= 2
        print("🔥 Critical Hit!")

    defender["health"] -= damage

    if defender["health"] < 0:
        defender["health"] = 0

    print(f"{attacker['name']} dealt {damage} damage.")


def use_potion():
    if player["potions"] > 0:
        player["potions"] -= 1
        player["health"] += 30

        if player["health"] > player["max_health"]:
            player["health"] = player["max_health"]

        game_log["potions_used"] += 1

        print("🧪 Potion Used!")
        print("Health:", player["health"])

    else:
        print("No Potions Left!")


def enemy_attack(enemy):
    roll = random.randint(0, 10)

    if roll < 2:
        print(enemy["name"], "missed the attack!")
        return

    damage = enemy["attack"] - player["defense"] + roll

    if damage < 0:
        damage = 0

    if roll > 8:
        damage *= 2
        print(enemy["name"], "Critical Hit!")

    player["health"] -= damage

    if player["health"] < 0:
        player["health"] = 0

    print(enemy["name"], "dealt", damage, "damage.")
def shop():
    while True:
        print("\n========== SHOP ==========")
        print("Gold:", player["gold"])
        print("1. Buy Attack (+5) = 30 Gold")
        print("2. Buy Potion = 20 Gold")
        print("3. Exit Shop")
        choice = input("Choice: ")
        if choice == "1":
            if player["gold"] >= 30:
                player["gold"] -= 30
                player["attack"] += 5
                print("Attack Increased!")
            else:
                print("Not enough Gold.")

        elif choice == "2":
            if player["gold"] >= 20:
                player["gold"] -= 20
                player["potions"] += 1
                print("Potion Purchased!")
            else:
                print("Not enough Gold.")

        elif choice == "3":
            break
        else:
            print("Invalid Input!")

def battle(enemy):
    print("\n========================")
    print("Enemy:", enemy["name"])
    print("========================")
    while enemy["health"] > 0 and player["health"] > 0:
        print("\nPlayer HP:", player["health"])
        print("Enemy HP :", enemy["health"])

        print("\n1.Attack")
        print("2.Heal")
        print("3.Run")

        choice = input("Choose: ")

        if choice == "1":

            attack_enemy(player, enemy)

            if enemy["health"] <= 0:
                print(enemy["name"], "Defeated!")

                player["gold"] += enemy["gold"]

                game_log["gold_earned"] += enemy["gold"]

                game_log["enemies_killed"] += 1

                print("Gold Earned:", enemy["gold"])
                return True

            enemy_attack(enemy)

        elif choice == "2":

            use_potion()

            enemy_attack(enemy)

        elif choice == "3":

            print("You Ran Away!")
            return False

        else:
            print("Invalid Input, try again.")

    return player["health"] > 0

# WAVES
waves = [
    ["Goblin1", "Goblin2"],
    ["Orc1", "Orc2"],
    ["Dragon"]
]

wave_no = 1

for wave in waves:
    print("\n========================")
    print("WAVE", wave_no)
    print("========================")
    for enemy_name in wave:
        alive = battle(enemies[enemy_name])
        if not alive:
            print("\nGAME OVER")
            break
    if player["health"] <= 0:
        break
    if wave_no != 3:
        shop()
    wave_no += 1
# FINAL RESULT
print("\n")
print("+--------------------------------------+")
print("|          FINAL BATTLE REPORT         |")
print("+----------------------+---------------+")
print(f"| Enemies Defeated     | {game_log['enemies_killed']:<13}|")
print(f"| Potions Used         | {game_log['potions_used']:<13}|")
print(f"| Gold Earned          | {game_log['gold_earned']:<13}|")
print(f"| Remaining Health     | {player['health']:<13}|")
print(f"| Remaining Potions    | {player['potions']:<13}|")
print(f"| Remaining Gold       | {player['gold']:<13}|")
print("+----------------------+---------------+")

if player["health"] > 0 and game_log["enemies_killed"] == 5:
    print("\n🏆 CONGRATULATIONS! You defeated the Dragon and won the game!")
else:
    print("\n💀 Better Luck Next Time!")