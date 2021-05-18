import pandas as pd
import random

def main():
    """ This is where the story occurs. We will have the main script here.
        Side effects:
             print(str): printing story
    """
    person = Person()
    extract = Extraction("extraction1.xlsx")
    
    name = Person.return_name()
    age = Person.return_age()
    gender = Person.return_gender()
    
    location = extract.location()
    item = extract.item()
    
    if gender == "female" or gender == "f":
        print(f"Once upon a time there was a {age} year old girl named {name}." 
              f" One day she was walking down a path in/on the" 
              f" {location} with a {item}. As she was walking down the path, she"
              f" was approached by an unidentified figure. At first she couldn't"
              f" see who it was, but as she got closer she realized it was {enemy}."
              f" She trembled in fear. She used her {item} to attack them.")
    elif gender == "male" or gender == "m":
        print(f"Once upon a time there was a {age} year old boy named {name}." 
              f" One day he was walking down a path in/on the {location} with a"
              f" {item}. As he was walking down the path, he"
              f" was approached by an unidentified figure. At first he couldn't"
              f" see who it was, but as he got closer he realized it was {enemy}."
              f" He trembled in fear. He used her {item} to attack them.")
    else: 
        print(f"Once upon a time there was a {age} year old person named {name}."
              f" One day they were walking down a path in/on the {location}"
              f" with a {item}. As they were walking down the path, they"
              f" were approached by an unidentified figure. At first they couldn't"
              f" see who it was, but as they got closer they realized it was {enemy}."
              f" They trembled in fear. They used their {item} to attack them.") 
    
    # make the storyline a sort of quest.
    # recomendations (you can do other stuff)
    # someone came to user with quest. get to __ but have to defeat 3 enemies on the way
    
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
            name(str): name of user
            damage(float): the damage implimented by the user's weapon
            hp(float): representing the user's health points
    """ 
    def __init__(self, name, damage, hp = 500):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def attack(self, opponent):
        """ Used to set attributes as objects.        
        Args:  
            opponent(str): the user's opponent
        Side effects:
            print(str): the printing of a line
        """
        damage = self.weapon_damage
        opponent.hp = opponent.hp - damage
        print("%s does %s damage to %s" % (self.name, damage, opponent.name))
    
class Enemy:
    """ Collect the information on enemy and turn it into an instance. 

        Attributes:
            name(str): name of Enemy
            damage(float): the damage implimented by the enemy
            hp(float): representing the enemy's health points
    """ 
    def __init__(self, name, damage, hp = 500):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def attack(self, opponent):
        """ Used to set attributes as objects.        
        Args:  
            opponent(str): the enemy's opponent
        Side effects:
            print(str): the printing of a line  
        """
        random = randint(0,1)
        if random == 0:
            print(f"{self.name} fails to do damage to {opponent.name}.")
        elif random == 1:
            damage = 
            opponent.hp = opponent.hp - damage
            print(f"{self.name} does {damage} damage to {opponent.name}.")
        
class Extraction:
    """ This is where we collect the random infomation from the csv file to
        incorprate into the story
        Attributes:
             
    """
    def __init__(self, filepath):
        """initializing new path object
            Attributes:
                filepath(str): location of csv file
        """
        self.df = pd.read_excel(filepath)
        
    def location(self):
        """ Getting random location from the csv file to fill in the script
            Returns: 
                location(str): location from csv file that is randomally picked
        """
        location_list = self.df["Location"].to_list()
        return (random.choice(location_list))
        
    def weapon(self):
        """Getting random weapon from csv file to fill in the script
            Returns:
                weapon(str): name of randomally picked weapon from csv file
        """
        weapon_list = self.df["Weapon"].to_list()
        return (random.choice(weapon_list))
        
    def enemy(self):
        """Getting random enemy from csv file to fill in the script
            Returns:
                enemy(str): name of randomally picked enemy from csv file
        """
        enemy_list = self.df["Enemy"].to_list()
        return (random.choice(enemy_list))
    
    def item(self):
        """ Getting random item from csv file to fill in the script
            Returns:
                item(str): name of randomally picked item from csv file
        """
        item_list = self.df["Item"].to_list()
        return (random.choice(item_list))
        
    def pet(self):
        """ Getting random pet from csv file to fill in the script
            Returns:
                pet(str): name of pet that is randomally picked from csv file
        """
        pet_list = self.df["Pet"].to_list()
        return (random.choice(pet_list))
    
    def weapon_damage(self):
        """ Getting random weapon_damage from csv file to fill in the script
            Returns:
                weapon_damage(int): damage of weapon that is randomally picked from csv file
        """
        weapon_damage_list = self.df["Weapon_damage"].to_list()
        return (random.choice(weapon_damage_list))
    
    def damage_dealt(self):
        """ Getting random damage_dealt from csv file to fill in the script
            Returns:
                damage_dealt(int): damage dealt that is randomally picked from csv file
        """
        damage_dealt_list = self.df["Damage_dealt"].to_list()
        return (random.choice(damage_dealt_list))
    
    def enemy_hp(self):
        """ Getting hp of enemy from csv file to fill in the script
            Returns:
                enemy_hp(int): hp of enemy that is randomally picked from csv file
        """
        enemy_hp_list = self.df["Hp"].to_list()
        return (random.choice(enemy_hp_list))
        
def battle(user, opp, pause = 2.0): 
    """ Stage a battle between user and enemy.
    
    Args:
        enemy (str): The name of the enemy, randomly taken from the csv file.
        user (str): Name of user, taken from user input.
        pause (float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 2.0.
        
    Side effects:
        print (string): printing play by play actions of battle
    """
    while user.hp > 0 and opp.hp > 0: 
        # user and enemy attack eachother 
        user.attack(opp)
        opp.attack(user)
    
        # print health points for each fighter
        print("%s has %s health points." % (a1.name, a1.hp))
        print("%s has %s health points." % (a2.name, a2.hp))
        
        # print blank line and wait 2 seconds
        print()
        sleep(pause)
    
    #print conclusion of battle
    if user.hp <= 0 and .hp <= 0:
        print("The battle ends in a draw. You have not completed your quest.")
    else: 
        if user.hp < opp.hp:
            print("%s wins. You have not completed your quest." % (opp.name))
        elif user.hp > opp.hp:
            print("%s wins! You get to move on." % (user.name))

if __name__ == "__main__":
    main()
