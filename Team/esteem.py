# page start
print()


def main():
    answer_list = []
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()
    print(
        "1. I feel that I am a person of worth, at least on an equal plane with others."
    )
    answer_list.append(input("Enter D, d, a, or A: "))
    print("2. I feel that I have a number of good qualities.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("3. All in all, I am inclined to feel that I am a failure.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("4. I am able to do things as well as most other people.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("5. I feel I do not have much to be proud of.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("6. I take a positive attitude toward myself.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("7. On the whole, I am satisfied with myself.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("8. I wish I could have more respect for myself.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("9. I certainly feel useless at times.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print("10. At times I think I am no good at all.")
    answer_list.append(input("Enter D, d, a, or A: "))
    print()
    print(f"Your score is {score(answer_list)}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def score(list):
    points = 0
    i = 0
    for x in list:
        i += 1
        if i == 1 or i == 2 or i == 4 or i == 6 or i == 7:
            if x == "D":
                points += 0
            elif x == "d":
                points += 1
            elif x == "a":
                points += 2
            else:
                points += 3
        else:
            if x == "D":
                points += 3
            elif x == "d":
                points += 2
            elif x == "a":
                points += 1
            else:
                points += 0

    return points


main()

# page end
print()
