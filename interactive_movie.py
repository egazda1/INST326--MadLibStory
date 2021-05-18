import pandas as pd
import random
from time import sleep
       
class Get1:
    """ Get information of the user.
    Attributes:
        user_name(str): name of the user.
        weapon_damage(int): weapon damage that the user can do to enemy.
        user_hp(int): health points of the user.
    """
    def __init__(self, user_name, weapon_damage, user_hp = 500):
        self.name = user_name
        self.damage = weapon_damage
        self.hp = user_hp
    
    def get_user(self, name):
        """ Used to return information of the user.        
        Args:  
            name(str): the user's name.
        Returns:
            the printing of information of the user.
        """
        name = self.name
        damage = self.damage
        hp = self.hp
        return User(name, damage, hp)

class Get2:
    """ Get information of the enemy.    
    Attributes:
        enemy_name(str): name of the enemy.
        enemy_damage(int): enemy damage that the enemy can do to user.
        enemy_hp(int): health points of the enemy.
    """
    def __init__(self, enemy_name, enemy_damage, enemy_hp):
        self.name = enemy_name
        self.damage = enemy_damage
        self.hp = enemy_hp
    
    def get_enemy(self, name):
        """ Used to list information of the enemy.        
        Args:  
            name(str): the enemy's name.
        Returns:
            the printing of information of the enemy.
        """
        name = self.name
        damage = self.damage
        hp = self.hp
        return Enemy(name, damage, hp)
    
class Person:
    """ Ask users to input their information, such as name, age and gender so they can become part of the game.
    Attributes:
        name(str): name of the user.
        age(int): age of the user.
        gender(str): gender of the user.
    """
    def __init__(self):
        self.name = str(input("Enter your name: "))
        self.age = int(input("Enter your age: "))
        self.gender = str(input("Enter your gender: "))
    
    def return_name(self):
        return self.name
        
    def return_age(self):
        return self.age
    
    def return_gender(self):
        return self.gender
    

class User:
    """ Collect the information on user and turn it into an instance. 
    Attributes:
        name(str): name of user.
        damage(int): the damage implimented by the user's weapon.
        hp(int): representing the user's health points.
    """ 
    def __init__(self, name, damage, hp = 500):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def attack(self, opponent):
        """ Used to set attributes as objects.        
        Args:  
            opponent(str): the user's opponent.
        Side effects:
            print(str): the printing of a line.
        """
        damage = self.damage
        opponent.hp = opponent.hp - damage
        print("%s does %s points of damage to %s" % (self.name, damage, opponent.name))
    
class Enemy:
    """ Collect the information on enemy and turn it into an instance. 
    Attributes:
        name(str): name of enemy.
        damage(int): the damage implimented by the enemy.
        hp(int): representing the enemy's health points.
    """ 
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def attack(self, opponent):
        """ Used to set attributes as objects.        
        Args:  
            opponent(str): the enemy's opponent.
        Side effects:
            print(str): the printing of a line.  
        """
        rand = random.randint(0, 1)
        
        if rand == 0:
            print(f"{self.name} fails to do any damage to {opponent.name}.")
        elif rand == 1:
            damage = self.damage
            opponent.hp = opponent.hp - damage
            print(f"{self.name} does {damage} points of damage to {opponent.name}.")
        
class Extraction:
    """ This is where we collect the random infomation from the csv file to
        incorprate into the story.
    Attributes:
        filepath(str): location of the csv file.    
    """
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)
        
    def location(self):
        """ Getting random location from the csv file to fill in the script.
        Returns: 
            location(str): location from csv file that is randomally picked.
        """
        location_list = self.df["Location"].to_list()
        return (random.choice(location_list))
        
    def weapon(self):
        """Getting random weapon from csv file to fill in the script.
        Returns:
            weapon(str): name of randomally picked weapon from csv file.
        """
        weapon_list = self.df["Weapons"].to_list()
        return (random.choice(weapon_list))
        
    def enemy(self):
        """Getting random enemy from csv file to fill in the script.
        Returns:
            enemy(str): name of randomally picked enemy from csv file.
        """
        enemy_list = self.df["Enemy"].to_list()
        return (random.choice(enemy_list))
    
    def item(self):
        """ Getting random item from csv file to fill in the script.
        Returns:
            item(str): name of randomally picked item from csv file.
        """
        item_list = self.df["Item"].to_list()
        return (random.choice(item_list))
        
    def pet(self):
        """ Getting random pet from csv file to fill in the script.
        Returns:
            pet(str): name of pet that is randomally picked from csv file.
        """
        pet_list = self.df["Pet"].to_list()
        return (random.choice(pet_list))
    
    def weapon_damage(self):
        """ Getting random weapon_damage from csv file to fill in the script.
        Returns:
            weapon_damage(int): damage of weapon that is randomally picked from csv file.
        """
        weapon_damage_list = self.df["Weapon_damage"].to_list()
        return (random.choice(weapon_damage_list))
    
    def damage_dealt(self):
        """ Getting random damage_dealt from csv file to fill in the script.
        Returns:
            damage_dealt(int): damage dealt that is randomally picked from csv file.
        """
        damage_dealt_list = self.df["Damage_dealt"].to_list()
        return (random.choice(damage_dealt_list))
    
    def enemy_hp(self):
        """ Getting hp of enemy from csv file to fill in the script.
        Returns:
            enemy_hp(int): hp of enemy that is randomally picked from csv file.
        """
        enemy_hp_list = self.df["Hp"].to_list()
        return (random.choice(enemy_hp_list))
        
def battle(user, opp, pause = 3.0): 
    """ Stage a battle between user and enemy.
    Args:
        user(str): The name of the enemy, randomly taken from the csv file.
        opp(str): Name of user, taken from user input.
        pause(float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 3.0.      
    Side effects:
        print(string): printing play by play actions of battle
    """
    while user.hp > 0 and opp.hp > 0: 
        # user and enemy attack eachother 
        user.attack(opp)
        opp.attack(user)
    
        # print health points for each fighter
        print("%s has %s health points." % (user.name, user.hp))
        print("%s has %s health points." % (opp.name, opp.hp))
        
        # print blank line and wait 2 seconds
        print()
        sleep(pause)
    
    #print conclusion of battle
    if user.hp <= 0 and opp.hp <= 0:
        print(f"Im sorry, this battle against {opp.name} has ended in a tie.")
        return 0
    elif user.hp < opp.hp: 
        print(f"Im sorry, you lost your battle against {opp.name}.")
        return 0
    elif user.hp > opp.hp:
        return 1

def main():
    """ This is where the story occurs. We will have the main script here.
        Side effect: printing story
    """
    person = Person()
    extract = Extraction("extraction1.xlsx")
    
    name = person.return_name()
    age = person.return_age()
    gender = person.return_gender()
    
    location = extract.location()
    item = extract.item()
    weapon = extract.weapon()
    enemy_name = extract.enemy()
    damage_dealt = extract.damage_dealt()
    enemy_hp = extract.enemy_hp()
    weapon_damage = extract.weapon_damage()
    
    if gender == "female" or gender == "f":
        print(f"Once upon a time there was a {age} year old girl named {name}. " 
              f"One day she was walking down a path in/on the " 
              f"{location} with a {item}.")
        
    elif gender == "male" or gender == "m":
        print(f"Once upon a time there was a {age} year old boy named {name}. " 
              f" One day he was walking down a path in/on the {location} with a "
              f" {item}. ")
    else: 
        print(f"Once upon a time there was a {age} year old person named {name}. "
              f" One day they were walking down a path in/on the {location} "
              f" with a {item}. ") 
      
    print(f"As they were walking down the path they were approached by a man who " 
         f"told them they must defeat 3 people to win the ultimate prize. They " 
         f"continued down the path and were first approached by an unidentified figure. " 
         f"As they got closer they realized it was {enemy_name}. They pulled out their {weapon} " 
         f" and attacked them. Their first battle started.")
    
    enemy = Get2(enemy_name, damage_dealt, enemy_hp).get_enemy(enemy_name)     
    user = Get1(name, weapon_damage).get_user(name)
    
    battle(user, enemy)
    if battle(user, enemy) == 1:
        print(f"Congrats {name}, you have defeated your first enemy. Continue " 
              f"along the path to find your next battle.")
        print()
        print(f"As they walked down the path they were soon stopped by another "
              f"person. They realized this person was {enemy.name}. They quickly "
              f"pulled out their {weapon} and the second battle began.")
        
        #create new enemy
        enemy_name2 = extract.enemy()
        enemy_hp2 = extract.enemy_hp()
        damage_dealt2 = extract.damage_dealt()
            
        enemy2 = Get2(enemy_name2, damage_dealt2, enemy_hp2).get_enemy(enemy_name)
        
        #run battle 
        battle(user,enemy2)
        
        if battle(user, enemy2) == 1:
            print(f"Congrats {name}, you have defeated your second enemy." 
                  f"You have one more to go. Continue down the path to find your " 
                  f"final battle. Not long after they were met with {enemy2.name}, " 
                  f"their third and final enemy. They pulled out their {weapon} "
                  f"and the third battle began.")
            
            #create new enemy
            enemy_name3 = extract.enemy()
            enemy_hp3 = extract.enemy_hp()
            damage_dealt3 = extract.damage_dealt()
            
            enemy3 = Get2(enemy_name3, damage_dealt3, enemy_hp3).get_enemy(enemy_name)
        
            #run battle 
            battle(user,enemy3)
            if battle(user, enemy3) == 1:
                
                print(f"Congrats {name}, you have defeated your three enemies " 
                      f"and have been rewarded the ultimate prize, a {item}.")
            
            elif battle(user, enemy3) == 0:
                print(f"Your story is completed.")
                
        elif battle(user, enemy2) == 0:
            print(f"Your story is completed.")
            
    elif battle(user, enemy) == 0:
        print(f"Your story is completed.")    

if __name__ == "__main__":
    main()
