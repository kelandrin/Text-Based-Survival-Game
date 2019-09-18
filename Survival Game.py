'''
ICS 31 Survival Game
Driver:  UCI_ID: 38916993  Name: Matthew Littman
'''
class Current_runtime:
    warrior = None
    monster = None
    room_number = 0

cr = Current_runtime() #global variable current_runtime

def main():
    monsters_dict = {}
    warriors_dict = {}
    intro()
    _continue_()
    intro_command_list()
    enter_warriors(warriors_dict)
    enter_monsters(monsters_dict)
    while True:
        command = read_command(warriors_dict,monsters_dict)
        if command == "cc":
            break
    story_room_one_monster(monsters_dict)
    fight()

class Warrior:
    name = ""
    attack = 0
    defence = 0
    strength = 0
    health = 100
    energy = 0
    potions = 0

class Monster:
    name = ""
    attack = 0
    defence = 0
    strength = 0
    health = 0
    energy = 0

def intro(): #prints intro message
    print("******* Welcome! *******")
    print("This is a text-based adventure game.")
    print("You will select your warrior and attempt to make your way through all 4 rooms to win!")
    print("There are 4 fierce monsters [Lesser_demon, Giant, Scorpion, Hydra] so prepare yourself for epic fights!" + "\n")
    print("You may choose one of four characters:")
    print("* Marth the Barbarian")
    print("* Silvec the Prince")
    print("* Lefra the Magician")
    print("* Celest the Archer")
    print("\n" + "Good luck!")

def intro_command_list(): #prints list of possible commands in the beginning
    print("\n" + "Please choose one of the following commands:")
    print("1. Print warrior's stats (PW)")
    print("2. Print all warrior's stats (PWS)")
    print("3. Print monster's stats (PM)")
    print("4. Print all monster's stats (PMS)")
    print("5. Choose character (CC)")
    print("6. Exit Program (X)" + "\n")

def story_room_one_monster(monsters_dict:dict): #prints story for room one
    random_monster(monsters_dict)
    cr.room_number = 1
    print("\n" + "Now that you have chosen your warrior,")
    print("let's suit up and prepare to fight!")
    print("You enter the first room and prepare to fight the",cr.monster.name, "\n")
    print("Here are the monster's stats:")
    print_faced_monster(monsters_dict)
    _continue_()
    print("\n" + "You may choose to attack with 4 different options." + "\n")
    print("Strong Attack: does more damage but uses more energy and higher chance of missing" +"\n"
          "Weak Attack: does less damage, but uses less energy and a lower chance of missing" + "\n"
          "Defend: greatly reduces amount of damage taken and takes very little energy" + "\n"
          "Rest: increases your energy" + "\n")

def _continue_(): #asks the user to press "c" to continue
    while True:
        if input("(Press enter to continue): ").lower() == "":
            break

def read_command(warriors_dict: dict,monsters_dict:dict)->str:  # reads users command and runs the correct function
    command = input("Please enter your command: ").lower()
    if command == "pw":
        print_warrior(warriors_dict)
    elif command == "pws":
        print_all_warriors(warriors_dict)
    elif command == "pm":
        print_monster(monsters_dict)
    elif command == "pms":
        print_all_monsters(monsters_dict)
    elif command == "cc":
        warrior_first_letter = get_warrior_decision()
        selected_warrior = assign_warrior(warrior_first_letter,warriors_dict)
        print_selected_warrior(warriors_dict)
        return command
    elif command == "x":
        exit()
    else:
        print("Invalid command")
    intro_command_list()

def read_file(file_name: str) -> list: #opens a file for reading and gathers the data into a list
    data = []
    file = open(file_name, "r")
    for line in file:
        data.append(line)
    file.close()
    return data

def make_warrior(name:str,attack:int,defence:int,strength:int,health:int,energy:int,potions:int): #creates warrior
    w = Warrior()
    w.name = name
    w.attack = float(attack)
    w.defence = float(defence)
    w.strength = float(strength)
    w.health = float(health)
    w.energy = int(energy)
    w.potions = int(potions)
    return w

def make_monster(name:str, attack:int,defence:int,strength:int,health:int,energy:int): #creates monster
    m = Monster()
    m.name = name
    m.attack = float(attack)
    m.defence = float(defence)
    m.health = float(health)
    m.strength = float(strength)
    m.energy = int(energy)
    return m

def enter_warriors(warriors_dict:dict): #reads file of warriors and enters stats into dict
    data = read_file("warriors.txt")
    for item in data:
        for stat in item:
            name, attack, defence, strength, health, energy, potions = item.split()
            warrior = make_warrior(name,attack,defence,strength,health,energy,potions)
            warriors_dict[name] = warrior

def enter_monsters(monsters_dict:dict): #reads file of monsters and enters stats into dict
    data = read_file("monsters.txt")
    for item in data:
        for stat in item:
            name, attack, defence, strength, health, energy = item.split()
            monster = make_monster(name,attack,defence,strength,health,energy)
            monsters_dict[name] = monster

def check_warrior(name:str, warriors_dict:dict)->bool: #checks if warrior exists in dict
    return name in warriors_dict

def check_monster(name:str, monsters_dict:dict)->bool: #checks if monster exists in dict
    return name in monsters_dict

def print_selected_warrior(warrior_dict:dict): #prints the stats of the selected warrior
    warrior = cr.warrior
    print("\n" + "Congrats!!!")
    print("You have selected:")
    print(warrior.name)
    print("Attack =",warrior.attack)
    print("Defence =",warrior.defence)
    print("Strength =",warrior.strength)
    print("Health =",warrior.health)
    print("Energy =",warrior.energy)
    print("Potion Count =",warrior.potions, "\n")
    _continue_()

def print_warrior(warriors_dict:dict): #asks user for name prints out the warrior's stats
    name = input("Which warrior would you like to look up by name: ").capitalize()
    if check_warrior(name,warriors_dict) != True:
        print("This warrior does not exist.")
    else:
        print(name)
        print("Attack =",warriors_dict[name].attack)
        print("Defence =",warriors_dict[name].defence)
        print("Strength =",warriors_dict[name].strength)
        print("Health =",warriors_dict[name].health)
        print("Energy =",warriors_dict[name].energy)
        print("Potion Count =",warriors_dict[name].potions, "\n")

def print_all_warriors(warriors_dict:dict): #prints out all of the warriors and their stats
    print("Here are all of the warriors: " + "\n")
    for warrior in warriors_dict.items():
        name = warrior[0]
        print(name)
        print("Attack =", warriors_dict[name].attack)
        print("Defence =", warriors_dict[name].defence)
        print("Strength =", warriors_dict[name].strength)
        print("Health =", warriors_dict[name].health)
        print("Energy =", warriors_dict[name].energy)
        print("Potion Count =", warriors_dict[name].potions, "\n")

def print_faced_monster(monster_dict:dict): #prints the stats of the monster faced
    print("\n" + cr.monster.name)
    print("Attack =",cr.monster.attack)
    print("Defence =",cr.monster.defence)
    print("Strength =",cr.monster.strength)
    print("Health =",cr.monster.health)
    print("Energy =",cr.monster.energy, "\n")

def print_monster(monsters_dict:dict): #prints out the monster's stats whose name you chose
    name = input("Which monster would you like to look up by name: ").capitalize()
    if check_monster(name,monsters_dict) != True:
        print("This monster does not exist.")
    else:
        print("\n" + name)
        print("Attack =",monsters_dict[name].attack)
        print("Defence =",monsters_dict[name].defence)
        print("Strength =",monsters_dict[name].strength)
        print("Health =",monsters_dict[name].health)
        print("Energy =",monsters_dict[name].energy, "\n")

def print_all_monsters(monsters_dict:dict): #prints out all of the monsters and their stats
    print("Here are all of the monsters: " + "\n")
    for monster in monsters_dict.items():
        name = monster[0]
        print(name)
        print("Attack =", monsters_dict[name].attack)
        print("Defence =", monsters_dict[name].defence)
        print("Strength =", monsters_dict[name].strength)
        print("Health =", monsters_dict[name].health)
        print("Energy =", monsters_dict[name].energy, "\n")

def find_warrior(name:str,warriors_dict:dict)-> Warrior: #searches dict for warrior and returns it
    for warrior in warriors_dict.items():
        if warrior[0] == name.capitalize():
            warrior = warriors_dict[name]
            x = True
            return warrior

def find_monster(name:str,monsters_dict:dict)-> Monster: #searches dict for monster and returns it
    for monster in monsters_dict.items():
        if monster[0] == name.capitalize():
            monster = monsters_dict[name]
            x = True
            return monster

def get_warrior_decision(): #asks user for warrior choice returns first letter of choice
    print("'m' = Marth" + "\n"
          "'s' = Silvec" + "\n"
          "'l' = Lefra" + "\n"
          "'c' = Celest" + "\n")
    while True:
        command = input("Select your warrior by entering the first letter of their name: ").lower()
        if command == 'm':
            break
        elif command == 's':
            break
        elif command == 'l':
            break
        elif command == 'c':
            break
        else:
            print("Invalid selection, please try again.")
    return command

def assign_warrior(command:str,warriors_dict:dict):  # takes letter and assigns character
    if command == "m":
        selected_warrior = find_warrior("Marth",warriors_dict)
        cr.warrior = selected_warrior
    elif command == "s":
        selected_warrior = find_warrior("Silvec",warriors_dict)
        cr.warrior = selected_warrior
    elif command == "l":
        selected_warrior = find_warrior("Lefra",warriors_dict)
        cr.warrior = selected_warrior
    elif command == "c":
        selected_warrior = find_warrior("Celest",warriors_dict)
        cr.warrior = selected_warrior

def print_health_warrior(): #prints warrior's current health
    print("Your current health is:",cr.warrior.health, "\n")

def print_health_monster(): #prints monster's current health
    print("The monster's current health is:",cr.monster.health, "\n")

def print_energy_warrior(): #prints warrior's current energy
    print("Your current Energy is:",cr.warrior.energy)

def print_energy_monster(): #prints monster's current energy
    print("The monster's current energy is:",cr.monster.energy)

def random_monster(monsters_dict: dict): #assigns a random monster to fight
    import random
    number = random.randint(1,len(monsters_dict.items()))
    for monster in monsters_dict.items():
        if number == 1:
            monster = find_monster("Lesser_demon",monsters_dict)
            cr.monster = monster
        elif number == 2:
            monster = find_monster("Giant",monsters_dict)
            cr.monster = monster
        elif number == 3:
            monster = find_monster("Scorpion",monsters_dict)
            cr.monster = monster
        elif number == 4:
            monster = find_monster("Hydra",monsters_dict)
            cr.monster = monster

def fight():
    while cr.monster.health > 0 and cr.warrior.health > 0:
        monster_attack = get_attack_monster()
        warrior_attack = get_attack_warrior()
        if warrior_turn(warrior_attack,monster_attack) == False:
            break
        else:
            monster_turn(warrior_attack,monster_attack)

def warrior_turn(warrior_attack:str, monster_attack:str):
    damage = assign_attack_warrior(warrior_attack)
    if check_if_warrior_defended(warrior_attack) != True:
        if check_if_monster_defended(monster_attack) == True:
            damage = .005 * (115 - cr.monster.defence) * damage
            if damage != 0:
                print("The monster has mostly defended your attack." + "\n")
        if assess_damage_to_monster(damage) == False:
            return False
    else:
        print("You have chosen to defend for your turn.")
        print_energy_warrior()
        print_health_monster()

def monster_turn(warrior_attack:str, monster_attack:str):
    damage = assign_attack_monster(monster_attack)
    if check_if_monster_defended(monster_attack) != True:
        if check_if_warrior_defended(warrior_attack) == True:
            damage = .005 * (115 - cr.warrior.defence) * assign_attack_monster(monster_attack)
            if damage != 0:
                print("You have mostly defended the monster's attack." + "\n")
        assess_damage_to_warrior(damage)
    else:
        print("The monster had chosen to defend for its turn.")
        print_energy_monster()
        print_health_warrior()
        _continue_()

def get_attack_warrior(): #asks user to enter their attack choice, returns choice
    print("'s' = 'Strong Attack (uses 3 energy)'")
    print("'w' = 'Weak Attack (uses 2 energy)'")
    print("'d' = 'Defend (uses 1 energy)'")
    print("'r' = 'Rest (recharges 3 energy)'" + "\n")
    while True:
        attack = input("Please select your move: ").lower()
        if energy_checks(attack) == True:
            if attack == 's':
                break
            elif attack == 'w':
                break
            elif attack == 'd':
                break
            elif attack == 'r':
                break
            else:
                print("Invalid Command" + "\n")
    return attack

def assign_attack_warrior(attack:str): #choose between strong attack, weak attack, defend, or rest
    if attack == 's':
        damage = warrior_strong_attack(attack)
        return damage
    elif attack == 'w':
        damage = warrior_weak_attack(attack)
        return damage
    elif attack == 'd':
        check_if_warrior_defended(attack)
        damage = warrior_defend()
        return damage
    elif attack == 'r':
        warrior_rest()
        damage = 0
        return damage

def warrior_strong_attack(attack:str)->int: #checks if attack misses, else warrior attacks strong and returns damage
    cr.warrior.energy -= 3
    result_chance = chance_of_missing_attack_warrior(attack)
    if result_chance == 'miss':
        print("The monster was too fast and your attack missed!")
        damage = 0
        return damage
    else:
        damage = .7 * cr.warrior.strength
        return damage

def warrior_weak_attack(attack)->int: #checks if attack misses, else warrior attacks weak and returns damage
    cr.warrior.energy -= 2
    result = chance_of_missing_attack_warrior(attack)
    if result == 'miss':
        print("The monster was too fast and your attack missed!")
        damage = 0
        return damage
    else:
        damage = .45 * cr.warrior.strength
        return damage

def warrior_defend(): #returns 0 damage and uses little energy
    cr.warrior.energy -= 1
    print("You prepare to defend the monster's attack")
    damage = 0
    return damage

def warrior_rest(): #returns 0 damage and restores 3 energy
    cr.warrior.energy += 3
    print("You rest and restore 3 energy!")
    damage = 0
    return damage

def get_attack_monster(): #uses randomization to decide which attack based on monsters energy
    if cr.monster.energy <= 6 and cr.monster.energy > 2:
        attack = randomize_monster_attack(4)
        return attack
    elif cr.monster.energy <= 2:
        attack = 'r'
        return attack
    else:
        attack = randomize_monster_attack(3)
        return attack

def randomize_monster_attack(number:int): #randomizes monsters attack
    import random
    number = random.randint(1,number)
    if number == 1:
        return 's'
    elif number == 2:
        return 'w'
    elif number == 3:
        return 'd'
    elif number == 4:
        return 'r'

def assign_attack_monster(attack:str): #assigns which attack to execute for monster
    if attack == 's':
        damage = monster_strong_attack(attack)
        return damage
    elif attack == 'w':
        damage = monster_weak_attack(attack)
        return damage
    elif attack == 'd':
        check_if_monster_defended(attack)
        damage = monster_defend()
        return damage
    elif attack == 'r':
        monster_rest()
        damage = 0
        return damage

def monster_strong_attack(attack): #checks if attack misses, else monster attacks strong and returns damage
    cr.monster.energy -= 3
    result_chance = chance_of_missing_attack_monster(attack)
    if result_chance == 'miss':
        print("You were too fast and the monster's attack missed!")
        damage = 0
        return damage
    else:
        damage = .2 * cr.monster.strength
        return damage

def monster_weak_attack(attack): #checks if attack misses, else monster attacks weak and returns damage
    cr.monster.energy -= 2
    result_chance = chance_of_missing_attack_monster(attack)
    if result_chance == 'miss':
        print("You were too fast and the monster's attack missed!")
        damage = 0
        return damage
    else:
        damage = .1 * cr.monster.strength
        return damage

def monster_defend(): #returns 0 damage and uses little energy
    cr.monster.energy -= 1
    damage = 0
    return damage

def monster_rest(): #returns 0 damage and restores 3 energy
    cr.monster.energy += 3
    print("The monster rests and restore 3 energy!")
    damage = 0
    return damage

def assess_damage_to_monster(damage:int)->bool: #takes in result(damage) of attack choice and applies the damage / checks for death
    cr.monster.health = cr.monster.health - damage
    print("You have done",damage,"damage!")
    print_energy_warrior()
    if check_if_monster_dead() == False:
        print_health_monster()
        _continue_()
        print("\n" + "Now the monster prepares to attack:")
        return True
    else:
        print("Congratulations! The",cr.monster.name,"is dead!!!")
        return False

def assess_damage_to_warrior(damage:int): #takes in result(damage) of attack choice and applies the damage / checks for death
        cr.warrior.health = cr.warrior.health - damage
        print("The monster has done", damage, "damage!")
        print_energy_monster()
        if check_if_warrior_dead() == False:
            print_health_warrior()
            _continue_()
            print("\n" + "Now you prepare to attack:")
        else:
            death()

def chance_of_missing_attack_warrior(attack:str)->str: #percent chance of warrior missing attack (higher attack means less missing)
    import random
    number = random.randint(1,cr.warrior.attack)
    if attack == 's' and number <= 20:
        result = 'miss'
        return result
    elif attack == 'w' and number <= 10:
        result = 'miss'
        return result

def chance_of_missing_attack_monster(attack:str)->str: #percent chance of warrior missing attack (higher attack means less missing)
    import random
    number = random.randint(1,cr.monster.attack)
    if attack == 's' and number <= 20:
        result = 'miss'
        return result
    elif attack == 'w' and number <= 10:
        result = 'miss'
        return result

def check_if_warrior_defended(attack:str)-> bool: #checks to see if warrior has defended
    defend = False
    if attack == 'd':
        defend = True
    return defend

def check_if_monster_defended(attack): #checks to see if monster has defended
    defend = False
    if attack == 'd':
        defend = True
    return defend

def check_if_enough_energy(attack:str)-> bool: #checks if you have enough energy to perform specific attack
    if attack == 's' and cr.warrior.energy < 3:
        return False
    elif attack == 'w' and cr.warrior.energy < 2:
        return False
    elif attack == 'd' and cr.warrior.energy < 1:
        return False
    elif attack == 'r':
        return True

def check_if_at_max_energy()-> bool: #checks if you are at max energy
    if cr.warrior.name == 'Marth' and cr.warrior.energy == 15:
        return True
    elif cr.warrior.name == 'Silvec' and cr.warrior.energy == 12:
        return True
    elif cr.warrior.name == 'Lefra' and cr.warrior.energy == 18:
        return True
    elif cr.warrior.name == 'Celest' and cr.warrior.energy == 21:
        return True

def energy_checks(attack)-> bool: #prints result if you are at max energy resting or dont have enough energy to attack returns bool
    check = True
    if check_if_enough_energy(attack) == False:
        print("You don't have enough energy for this attack" + "\n")
        check = False
    if check_if_at_max_energy() == True and attack == 'r':
        print("You are trying to rest at full health" + "\n")
        check = False
    return check

def check_if_warrior_dead()->bool: #checks to see if warrior died
    if cr.warrior.health > 0:
        return False

def check_if_monster_dead()->bool: #checks to see if monster died
    if cr.monster.health > 0:
        return False

def death(): #prints end message if you die
    print("\n" + "Oh no! It seems the",cr.monster.name,"has killed you!")
    print("Good Game!")
    print("*******************************")
    exit()

'''
def take_potion(): #increase health with potion (can only take before the start of a room)

def potion_potency(): #potion gets stronger over time

def win(): #what happens when you win


def room_1(): #details of room 1

def room_2(): #details of room 2

def room_3(): #details of room 3

def room_4(): #details of room 4

def proceed_to_next_room():  #proceeds to next room


def chance_of_success_for_running():

def chance_of_poison():

def poison():


'''








if __name__ == "__main__":
    main()