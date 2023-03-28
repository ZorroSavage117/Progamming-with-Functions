import dice
import dice2
import saving
import pytest 

def test_roll_d4():
    assert 0 <= dice.roll_d4() <= 4

def test_roll_d_unknown():
    assert 0 <= dice.roll_d_unknown(25) <= 25

def test_find_key():
    assert saving.find_key(25) == 'd?'

def test_sum_of_rolls():
    rolls = [4, 20, 6, 10]
    assert dice2.sum_of_rolls(rolls) == 40


pytest.main(["-v", "--tb=line", "-rN", __file__])