import random

def roll_d4():
    """
    Retures a random number between 1 and 4
    """
    roll = random.randint(1, 4)

    return roll

def roll_d8():
    """
    Retures a random number between 1 and 8
    """
    roll = random.randint(1, 8)

    return roll

def roll_d12():
    """
    Retures a random number between 1 and 12
    """
    roll = random.randint(1, 12)

    return roll

def roll_d20():
    """
    Retures a random number between 1 and 20
    """
    roll = random.randint(1, 20)

    return roll

def roll_d6():
    """
    Retures a random number between 1 and 6
    """
    roll = random.randint(1, 6)

    return roll

def roll_d10():
    """
    Retures a random number between 1 and 10
    """
    roll = random.randint(1, 10)

    return roll

def roll_d100():
    """
    Retures a random number between 1 and 100
    """
    roll = random.randint(1, 100)

    return roll

def roll_d_unknown(max_number):
    """
    Retures a random number between 1 and user input
    """
    roll = random.randint(1, max_number)

    return roll

# test_d4_1 = roll_d4()
# test_d4_2 = roll_d4()
# test_d4_3 = roll_d4()
# print(f"4:{test_d4_1} | {test_d4_2} | {test_d4_3}")

# test_d8_1 = roll_d8()
# test_d8_2 = roll_d8()
# test_d8_3 = roll_d8()
# print(f"8:{test_d8_1} | {test_d8_2} | {test_d8_3}")

# test_d12_1 = roll_d12()
# test_d12_2 = roll_d12()
# test_d12_3 = roll_d12()
# print(f"12:{test_d12_1} | {test_d12_2} | {test_d12_3}")

# test_d20_1 = roll_d20()
# test_d20_2 = roll_d20()
# test_d20_3 = roll_d20()
# print(f"20:{test_d20_1} | {test_d20_2} | {test_d20_3}")

# test_d6_1 = roll_d6()
# test_d6_2 = roll_d6()
# test_d6_3 = roll_d6()
# print(f"6:{test_d6_1} | {test_d6_2} | {test_d6_3}")

# test_d10_1 = roll_d10()
# test_d10_2 = roll_d10()
# test_d10_3 = roll_d10()
# print(f"10:{test_d10_1} | {test_d10_2} | {test_d10_3}")

# test_d100_1 = roll_d100()
# test_d100_2 = roll_d100()
# test_d100_3 = roll_d100()
# print(f"100:{test_d100_1} | {test_d100_2} | {test_d100_3}")

# test_d_1 = roll_d_unknown(35)
# test_d_2 = roll_d_unknown(40)
# test_d_3 = roll_d_unknown(750)
# print(f"35:{test_d_1} | 40:{test_d_2} | 750:{test_d_3}")