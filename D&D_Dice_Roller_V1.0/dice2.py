import dice

def roll_x_dice(number_of_dice, sides):
    """
    Rolls a specified number of dice with a specified number of sides, and returns a list of the rolls.
    :param number_of_dice: The number of dice to be rolled.
    :param sides: The number of sides on each die.
    """
    rolls = []
    count = 0
    
    # Rolls a specified number of dice with the specified number of sides, based on the given input
    if sides == 20:
        while count != number_of_dice:
            roll = dice.roll_d20()
            rolls.append(roll)
            count += 1
    elif sides == 6:
        while count != number_of_dice:
            roll = dice.roll_d6()
            rolls.append(roll)
            count += 1
    elif sides == 8:
        while count != number_of_dice:
            roll = dice.roll_d8()
            rolls.append(roll)
            count += 1
    elif sides == 4:
        while count != number_of_dice:
            roll = dice.roll_d4()
            rolls.append(roll)
            count += 1
    elif sides == 10:
        while count != number_of_dice:
            roll = dice.roll_d10()
            rolls.append(roll)
            count += 1
    elif sides == 12:
        while count != number_of_dice:
            roll = dice.roll_d12()
            rolls.append(roll)
            count += 1
    elif sides == 100:
        while count != number_of_dice:
            roll = dice.roll_d100()
            rolls.append(roll)
            count += 1
    else:
        while count != number_of_dice:
            roll = dice.roll_d_unknown(sides)
            rolls.append(roll)
            count += 1

    return rolls


def sum_of_rolls(list_of_rolls):
    """
    Returns the total sum of a list of dice rolls.
    :param list_of_rolls: A list of the dice rolls to be summed.
    """
    total = 0
    for roll in list_of_rolls:
        total += roll

    return total
