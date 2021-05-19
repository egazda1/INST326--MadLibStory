""" pytest for interactive_movie.py"""
from pytest import approx, fixture
import random
import pytest
import myproject
import re
import interactive_movie as movie
import builtins
from unittest import mock

def test_Person_init():
    with mock.patch("builtins.input", side_effect=["James", 22, "m"]):
        assert movie.Person.return_name() == ("James")
        assert movie.Person.return_age() == (22)
        assert movie.Person.return_gender() == ("m")

def test_attack(capsys):
    test_user = movie.User("George", 60, 700)
    test_enemy = movie.Enemy("Joker", 86, 450)
    test_user.attack(test_enemy)
    outerr = capsys.readouterr()
    out = outerr.out
    assert out == "George does 60 points of damage to Joker"

@fixture
def user1():
    return movie.User("Vincent", 120)

@fixture
def user2():
    return movie.User("Lenny", 99)

@fixture
def user3():
    return movie.User("Gina", 100)

def test_user_name(user1):
    """Is the User's name attribute assigned as expected?"""
    assert hasattr(user1, "name"), "User has no 'name' attribute"
    assert user1.name == "Vincent", \
        f"name attribute has unexpected value {user1.name}"
    
def test_user_damage(user1):
    """Is the User's damage attribute assigned as expected?"""
    assert hasattr(user1, "hp"), "User has no 'damage' attribute"
    assert user1.damage == approx(120), \
        f"hp attribute has unexpected value {user1.damage}"
    
def test_user_hp(user1):
    """Is the User's hp attribute assigned as expected?"""
    assert hasattr(user1, "hp"), "User has no 'hp' attribute"
    assert user1.hp == approx(500), \
        f"hp attribute has unexpected value {user1.hp}"
    
@fixture
def enemy1():
    return movie.Enemy("Mr. Crocker", 60, 300)

@fixture
def enemy2():
    return movie.Enemy("Mr. Burns", 75, 400)

@fixture
def enemy3():
    return movie.Enemy("Joker", 87, 500)
    
def test_enemy_name(enemy1):
    """Is the Enemy's name attribute assigned as expected?"""
    assert hasattr(enemy1, "name"), "Enemy has no 'name' attribute"
    assert enemy1.name == "Mr. Crocker", \
        f"name attribute has unexpected value {enemy1.name}"
    
def test_enemy_damage(enemy1):
    """Is the User's damage attribute assigned as expected?"""
    assert hasattr(enemy1, "hp"), "Enemy has no 'damage' attribute"
    assert enemy1.damage == approx(60), \
        f"hp attribute has unexpected value {enemy1.damage}"
    
def test_enemy_hp(enemy1):
    """Is the User's hp attribute assigned as expected?"""
    assert hasattr(enemy1, "hp"), "Enemy has no 'hp' attribute"
    assert enemy1.hp == approx(300), \
        f"hp attribute has unexpected value {enemy1.hp}"

#docstrings
def test_get1_docstring_exists():
    """Does Get1 class have a class docstring?"""
    docstr = movie.Get1.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Get1 class has no class docstring"

def test_get1_docstring_contents():
    """Does Get1 class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.Get1.__doc__, \
        "Get1 class docstring has no 'Attributes:' section"

def test_get_user_docstring_exists():
    """Does get_user() have a docstring?"""
    docstr = movie.Get1.get_user.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "get_user() method has no docstring"

def test_get_user_docstring_contents():
    """Does get_user() docstring have the correct sections?"""
    docstr = movie.Get1.get_user.__doc__
    assert "Args:" in docstr, \
        "get_user() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "get_user() method docstring has no 'Returns:' section"

def test_get2_docstring_exists():
    """Does Get2 class have a class docstring?"""
    docstr = movie.Get2.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Get2 class has no class docstring"

def test_get2_docstring_contents():
    """Does Get2 class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.Get2.__doc__, \
        "Get2 class docstring has no 'Attributes:' section"

def test_get_enemy_docstring_exists():
    """Does get_enemy() have a docstring?"""
    docstr = movie.Get2.get_enemy.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "get_enemy() method has no docstring"

def test_get_enemy_docstring_contents():
    """Does get_enemy() docstring have the correct sections?"""
    docstr = movie.Get2.get_enemy.__doc__
    assert "Args:" in docstr, \
        "get_enemy() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "get_enemy() method docstring has no 'Returns:' section"
    
def test_person_docstring_exists():
    """Does Person class have a class docstring?"""
    docstr = movie.Person.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Person class has no class docstring"

def test_person_docstring_contents():
    """Does Person class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.Person.__doc__, \
        "Person class docstring has no 'Attributes:' section"
    
def test_return_name_docstring_exists():
    """Does return_name() have a docstring?"""
    docstr = movie.Person.return_name.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "return_name() method has no docstring"

def test_return_name_docstring_contents():
    """Does return_name() docstring have the correct sections?"""
    docstr = movie.Person.return_name.__doc__
    assert "Args:" in docstr, \
        "return_name() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "return_name() method docstring has no 'Returns:' section"
    
def test_return_age__docstring_exists():
    """Does return_age() have a docstring?"""
    docstr = movie.Person.return_age.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "return_age() method has no docstring"

def test_return_age_docstring_contents():
    """Does return_age() docstring have the correct sections?"""
    docstr = movie.Person.return_age.__doc__
    assert "Args:" in docstr, \
        "return_age() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "return_name() method docstring has no 'Returns:' section"

def test_return_gender_docstring_exists():
    """Does return_gender() have a docstring?"""
    docstr = movie.Person.return_gender.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "return_gender() method has no docstring"

def test_return_gender_docstring_contents():
    """Does return_gender() docstring have the correct sections?"""
    docstr = movie.Person.return_gender.__doc__
    assert "Args:" in docstr, \
        "return_gender() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "return_name() method docstring has no 'Returns:' section"
        
def test_user_docstring_exists():
    """Does User class have a class docstring?"""
    docstr = movie.User.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "User class has no class docstring"

def test_user_docstring_contents():
    """Does User class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.User.__doc__, \
        "User class docstring has no 'Attributes:' section"

def test_attack_docstring_exists():
    """Does attack() have a docstring?"""
    docstr = movie.User.attack.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "attack() method has no docstring"
        
def test_attack_docstring_contents():
    """Does attack() docstring have the correct sections?"""
    docstr = movie.User.attack.__doc__
    assert "Args:" in docstr, \
        "attack() method docstring has no 'Args:' section"
    assert "Side Effects:" in docstr, \
        "attack() method docstring has no 'Side Effects:' section"

def test_enemy_docstring_exists():
    """Does Enemy class have a class docstring?"""
    docstr = movie.Enemy.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Enemy class has no class docstring"
    
def test_enemy_docstring_contents():
    """Does Enemy class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.Enemy.__doc__, \
        "Enemy class docstring has no 'Attributes:' section"

def test_attack_enemy_docstring_exists():
    """Does attack() have a docstring?"""
    docstr = movie.Enemy.attack.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "attack() method has no docstring"

def test_attack_enemy_docstring_contents():
    """Does attack() docstring have the correct sections?"""
    docstr = movie.Enemy.attack.__doc__
    assert "Args:" in docstr, \
        "attack() method docstring has no 'Args:' section"
    assert "Side Effects:" in docstr, \
        "attack() method docstring has no 'Side Effects:' section"

def test_extraction_docstring_exists():
    """Does Extraction class have a class docstring?"""
    docstr = movie.Extraction.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Extraction class has no class docstring"

def test_extraction_docstring_contents():
    """Does Extraction class docstring have an Attributes: section?"""
    assert "Attributes:" in movie.Extraction.__doc__, \
        "Extraction class docstring has no 'Attributes:' section"
        
def test_location_docstring_exists():
    """Does location() have a docstring?"""
    docstr = movie.Extraction.location.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "location() method has no docstring"

def test_location_docstring_contents():
    """Does location() docstring have the correct sections?"""
    docstr = movie.Extraction.location.__doc__
    assert "Args:" in docstr, \
        "location() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "location() method docstring has no 'Returns:' section"
        
def test_weapon_docstring_exists():
    """Does weapon() have a docstring?"""
    docstr = movie.Extraction.weapon.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "weapon() method has no docstring"

def test_weapon_docstring_contents():
    """Does weapon() docstring have the correct sections?"""
    docstr = movie.Extraction.weapon.__doc__
    assert "Args:" in docstr, \
        "weapon() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "weapon() method docstring has no 'Returns:' section"      
        
def test_enemy_docstring_exists():
    """Does enemy() have a docstring?"""
    docstr = movie.Extraction.enemy.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "enemy() method has no docstring"

def test_enemy_docstring_contents():
    """Does enemy() docstring have the correct sections?"""
    docstr = movie.Extraction.enemy.__doc__
    assert "Args:" in docstr, \
        "enemy() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "enemy() method docstring has no 'Returns:' section"  
        
def test_item_docstring_exists():
    """Does item() have a docstring?"""
    docstr = movie.Extraction.item.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "item() method has no docstring"

def test_item_docstring_contents():
    """Does item() docstring have the correct sections?"""
    docstr = movie.Extraction.item.__doc__
    assert "Args:" in docstr, \
        "item() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "item() method docstring has no 'Returns:' section"  
        
def test_pet_docstring_exists():
    """Does pet() have a docstring?"""
    docstr = movie.Extraction.pet.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "pet() method has no docstring"

def test_pet_docstring_contents():
    """Does pet() docstring have the correct sections?"""
    docstr = movie.Extraction.pet.__doc__
    assert "Args:" in docstr, \
        "pet() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "pet() method docstring has no 'Returns:' section"  
        
def test_weapon_damage_docstring_exists():
    """Does weapon_damage() have a docstring?"""
    docstr = movie.Extraction.weapon_damage.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "weapon_damage() method has no docstring"

def test_weapon_damage_docstring_contents():
    """Does weapon_damage() docstring have the correct sections?"""
    docstr = movie.Extraction.weapon_damage.__doc__
    assert "Args:" in docstr, \
        "weapon_damage() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "weapon_damage() method docstring has no 'Returns:' section"  
        
def test_damage_dealt_docstring_exists():
    """Does damage_dealt() have a docstring?"""
    docstr = movie.Extraction.damage_dealt.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "damage_dealt() method has no docstring"

def test_damage_dealt_docstring_contents():
    """Does damage_dealt() docstring have the correct sections?"""
    docstr = movie.Extraction.damage_dealt.__doc__
    assert "Args:" in docstr, \
        "damage_dealt() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "damage_dealt() method docstring has no 'Returns:' section"  
        
def test_enemy_hp_docstring_exists():
    """Does enemy_hp() have a docstring?"""
    docstr = movie.Extraction.enemy_hp.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "enemy_hp() method has no docstring"

def test_enemy_hp_docstring_contents():
    """Does enemy_hp() docstring have the correct sections?"""
    docstr = movie.Extraction.enemy_hp.__doc__
    assert "Args:" in docstr, \
        "enemy_hp() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "enemy_hp() method docstring has no 'Returns:' section"  

def test_battle_docstring_exists():
    """Does battle() have a docstring?"""
    docstr = movie.battle.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "battle() method has no docstring"

def test_battle_docstring_contents():
    """Does battle() docstring have the correct sections?"""
    docstr = movie.battle.__doc__
    assert "Args:" in docstr, \
        "battle() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "battle() method docstring has no 'Returns:' section"
    assert "Side Effects:" in docstr, \
        "battle() method docstring has no 'Side Effects:' section"

def test_main_docstring_exists():
    """Does main() have a docstring?"""
    docstr = movie.main.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "main() method has no docstring"

def test_main_docstring_contents():
    """Does main() docstring have the correct sections?"""
    docstr = movie.main.__doc__
    assert "Args:" in docstr, \
        "main() method docstring has no 'Args:' section"
    assert "Side Effects:" in docstr, \
        "main() method docstring has no 'Side Effects:' section"
