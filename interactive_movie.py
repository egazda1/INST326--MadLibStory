import pandas as pd
import random

def main():
    """ This is where the story occurs. We will have the main script here.
        Side effect: printing story
    """
    person = Player()
    extract = Extraction("extraction1.xlsx")
    
    name = person.return_name()
    age = person.return_age()
    gender = person.return_gender()
    
    location = extract.location()
    item = extract.item()
    
    if gender == "female" or gender == "f":
        print(f"Once upon a time there was a {age} year old girl named {name}." 
              f" One day she was walking down a path in/on the" 
              f" {location} with a {item}.")
    elif gender == "male" or gender == "m":
        print(f"Once upon a time there was a {age} year old boy named {name}." 
              f" One day he was walking down a path in/on the {location} with a"
              f" {item}.")
    else: 
        print(f"Once upon a time there was a {age} year old person named {name}."
              f" One day they were walking down a path in/on the {location}"
              f" with a {item}.") 
              
    
class Player():
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
    
class Fighter:
    """ Collect the information on enemy and turn it into an instance. 

        Attributes:
            name(str): name of fighter
            damage(float): the damage implimented by the enemy/ or the damage 
            implimented by the user and their weapon.
            hp(float): representing the fighter's health points
    """ 
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp
        
    def attack(self, opponent):
        """ Used to set attributes as objects.        
        Args:  
            opponent: the aardvark’s opponent
        Side effects:
            the printing of a line  
        """
        
class Extraction:
    """ This is where we collect the random infomation from the csv file to
        incorprate into the story
        
         
    """
    def __init__(self, filepath):
        """initializing new path object
            attributes:
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
        
class Fight():
    """ Show the results of the battle, such as the remaining HP of the player and the enemy
    """
        
    def attack():
        """ Getting the result of an attack
            Returns:
                damage(int): how many damage was made from this attack
        """
        
    def hp_of_player(hp = 500):
        """ Getting the remain HP of the player
            Returns:
                hp_of_player(int): The remaining hp of the player
        """
        
    def hp_of_enemy():
        """ Getting the remain HP of the enemy
            Returns:
                hp_of_enemy(int): The remaining hp of the enemy
        """
        
def battle(user, opp, pause = 2.0): 
    """ Stage a battle between user and enemy.
    
    Args:
        enemy (str): The name of the enemy, randomly taken from the csv file.
        user (str): Name of user, taken from user input.
        pause (float): an amount of time in seconds to pause between attacks in
            a battle. Allows the user time to read the outcome of each attack.
            Default: 2.0.
        
    Side effects:
        print (string): printing play by play actions 
    """
    

if __name__ == "__main__":
    main()
