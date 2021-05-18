""" pytest for interactive_movie.py"""
from pytest import approx, fixture
import random
import re
import interactive_movie as movie

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
    assert "Side effects:" in docstr, \
        "get_enemy() method docstring has no 'Side effects:' section"
    
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
    assert "Side effects:" in docstr, \
        "return_name() method docstring has no 'Side effects:' section"
    
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
    assert "Side effects:" in docstr, \
        "return_age() method docstring has no 'Side effects:' section"

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
    assert "Side effects:" in docstr, \
        "return_gender() method docstring has no 'Side effects:' section"
        
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
    assert "Returns:" in docstr, \
        "attack() method docstring has no 'Returns:' section"

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
    assert "Returns:" in docstr, \
        "attack() method docstring has no 'Returns:' section"