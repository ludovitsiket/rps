import sys, random

choices = ("rock", "paper", "scissors")

def formating(string_value):
    unformated_string = str(string_value)
    possibilities = ("(", "'", ")", ",")
    for symbol in unformated_string:
        unformated_string = unformated_string.replace(symbol,"")
    return unformated_string

def menu(choices):
    formated_string = formating(choices)
    print('Choices: ',formated_string)
    print('For exit game press x.')

def game_result(player_choice, computer_choice):
    p_ch = player_choice
    c_ch = computer_choice
    if p_ch == c_ch:
        result = "Tie!"
    elif (p_ch=="rock" and c_ch=="scissors") or (p_ch=="paper" and c_ch=="rock") or (p_ch=="scissors" and c_ch=="paper"):
        result = "Player win !"
    else:
        result = "Computer win !"
    return result

def main():
    menu(choices)
    player_choice = input("Enter your choice: ")
    if True:
        if player_choice in choices:
                print("player choice", player_choice)
                index = random.randint(0,2)
                computer_choice = choices[index]
                print("computer choice:", computer_choice)
                result = game_result(player_choice, computer_choice)
                print(result)
                main()
        else:
            if player_choice == "x":
                print("Bye.")
                sys.exit(0)
            else:
                main()

main()
