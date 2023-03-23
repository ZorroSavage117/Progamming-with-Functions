import random

def roll_d4():
    """
    Returns a random number between 1 and 4 (inclusive).
    """
    roll = random.randint(1, 4)

    return roll

def roll_d8():
    """
    Returns a random number between 1 and 8 (inclusive).
    """
    roll = random.randint(1, 8)

    return roll

def roll_d12():
    """
    Returns a random number between 1 and 12 (inclusive).
    """
    roll = random.randint(1, 12)

    return roll

def roll_d20():
    """
    Returns a random number between 1 and 20 (inclusive).
    """
    roll = random.randint(1, 20)

    return roll

def roll_d6():
    """
    Returns a random number between 1 and 6 (inclusive).
    """
    roll = random.randint(1, 6)

    return roll

def roll_d10():
    """
    Returns a random number between 1 and 10 (inclusive).
    """
    roll = random.randint(1, 10)

    return roll

def roll_d100():
    """
    Returns a random number between 1 and 100 (inclusive).
    """
    roll = random.randint(1, 100)

    return roll

def roll_d_unknown(max_number):
    """
    Returns a random number between 1 and the specified maximum number (inclusive).
    :param max_number: The upper limit for the random number.
    """
    roll = random.randint(1, max_number)

    return roll
