#!/usr/bin/env python3

import datetime
import random
import sys

choices = ("r", "p", "s")
player_score = 0
computer_score = 0


def formating(string_value):
    unformated = str(string_value)
    possibilities = ("(", "'", ")", ",")
    for symbol in possibilities:
        unformated = unformated.replace(symbol, "")
        formated_string = unformated
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


def game_result(ch1, ch2, value1, value2):
    if ch1 == ch2:
        result = "Tie!"
    elif (
        ch1 == "rock" and ch2 == "scissors") or (
            ch1 == "paper" and ch2 == "rock") or (
            ch1 == "scissors" and ch2 == "paper"):
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
    sys.exit(0)


def exit_game(choice, value1, value2):
    if choice == "x":
        save_to_file(value1, value2)
    else:
        game(value1, value2)
    sys.exit(0)


def game(v1, v2):
    try:
        pl_ch = input("Enter your choice: ")
        if pl_ch in choices:
            computer_choice = game_progress()
            result, v1, v2 = game_result(pl_ch, computer_choice, v1, v2)
            print(result)
            game(v1, v2)
        else:
            exit_game(pl_ch, v1, v2)
    except NameError:
        require()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)


def main():
    menu(choices)
    game(player_score, computer_score)


if __name__ == '__main__':
    main()
