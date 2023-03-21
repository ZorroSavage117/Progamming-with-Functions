import dice

def roll_x_dice(number_of_dice, sides):
    rolls = []
    count = 0
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
    total = 0
    for roll in list_of_rolls:
        total += roll

    return total

# print("test d8")
# test1_lt = roll_x_dice(5, 8)
# test1_total = sum_of_rolls(test1_lt)
# print(f"list: {test1_lt}")
# print(f"total: {test1_total}")

# print("test d12")
# test2_lt = roll_x_dice(5, 12)
# test2_total = sum_of_rolls(test2_lt)
# print(f"list: {test2_lt}")
# print(f"total: {test2_total}")

# print("test d20")
# test3_lt = roll_x_dice(5, 20)
# test3_total = sum_of_rolls(test3_lt)
# print(f"list: {test3_lt}")
# print(f"total: {test3_total}")

# print("test d10")
# test4_lt = roll_x_dice(5, 10)
# test4_total = sum_of_rolls(test4_lt)
# print(f"list: {test4_lt}")
# print(f"total: {test4_total}")

# print("test d12")
# test5_lt = roll_x_dice(5, 12)
# test5_total = sum_of_rolls(test5_lt)
# print(f"list: {test5_lt}")
# print(f"total: {test5_total}")

# print("test d6")
# test6_lt = roll_x_dice(5, 6)
# test6_total = sum_of_rolls(test6_lt)
# print(f"list: {test6_lt}")
# print(f"total: {test6_total}")

# print("test d?")
# test7_lt = roll_x_dice(5, 506)
# test7_total = sum_of_rolls(test7_lt)
# print(f"list: {test7_lt}")
# print(f"total: {test7_total}")

# print("test d4")
# test8_lt = roll_x_dice(5, 4)
# test8_total = sum_of_rolls(test8_lt)
# print(f"list: {test8_lt}")
# print(f"total: {test8_total}")

# print("test d100")
# test9_lt = roll_x_dice(5, 100)
# test9_total = sum_of_rolls(test9_lt)
# print(f"list: {test9_lt}")
# print(f"total: {test9_total}")