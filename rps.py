#!/usr/bin/env python3

import datetime
import random
import sys

choices = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0


# noinspection PyUnboundLocalVariable
def formating(string_value):
    unformated_string = str(string_value)
    possibilities = ("(", "'", ")", ",")
    for symbol in possibilities:
        unformated_string = unformated_string.replace(symbol, "")
        formated_string = unformated_string
    return formated_string


def logo(text):
    count = len(text)
    print("-" * count)
    print(text)
    print("-" * count)


def menu(values):
    text = "rock - paper - scissors"
    logo(text)
    formated_string = formating(values)
    print('Choices: ', formated_string)
    print('For exit game press x.')


def require():
    print("Script require python 3.x for properly function.")
    sys.exit(0)


def game_result(choice1, choice2, value1, value2):
    if choice1 == choice2:
        result = "Tie!"
    elif (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (
            choice1 == "scissors" and choice2 == "paper"):
        value1 += 1
        result = "Player win !"
    else:
        value2 += 1
        result = "Computer win !"
    return result, value1, value2


def actual_date():
    now = str(datetime.datetime.now())
    date = (now[:-10])
    return date


def writing_score(value):
    score_file = "score.txt"
    with open(score_file, "a+") as score:
        score.write(value + "\n")


def high_score(value1, value2):
    result = ("Player score:", value1, "    Computer score:", value2)
    result = formating(result)
    print(result)
    date = actual_date()
    to_file = (date + " :" + "      " + result)
    return to_file


def game_progress():
    index = random.randint(0, 2)
    computer_choice = choices[index]
    print("Computer choice:", computer_choice)
    return computer_choice


def save_to_file(value1, value2):
    print("Bye.")
    to_file = high_score(value1, value2)
    writing_score(to_file)
    sys.exit()


def exit_game(choice, value1, value2):
    if choice == "x":
        save_to_file(value1, value2)
    else:
        game(value1, value2)


def game(value1, value2):
    try:
        player_choice = input("Enter your choice: ")
        if player_choice in choices:
            computer_choice = game_progress()
            result, value1, value2 = game_result(player_choice, computer_choice, value1,
                                                 value2)
            print(result)
            game(value1, value2)
        else:
            exit_game(player_choice, value1, value2)
            pass
    except NameError:
        require()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit()


def main():
    menu(choices)
    game(player_score, computer_score)


main()
