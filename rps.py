import sys, random, datetime

choices = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

def formating(string_value):
    unformated_string = str(string_value)
    possibilities = ("(", "'", ")", ",")
    for symbol in possibilities:
        unformated_string = unformated_string.replace(symbol ,"")
        formated_string = unformated_string
    return formated_string

def logo(text):
    count = len(text)
    print("-"*count) 
    print(text)
    print("-"*count)

def menu(choices):
    text = "Rock - Paper - Scissors"
    logo(text)
    formated_string = formating(choices)
    print('Choices: ',formated_string)
    print('For exit game press x.')

def require():
    print("Script require python 3.x for properly function.")
    sys.exit(0)

def game_result(player_choice, computer_choice, player_score, computer_score):
    p_ch = player_choice
    c_ch = computer_choice
    if p_ch == c_ch:
        result = "Tie!"
    elif (p_ch=="rock" and c_ch=="scissors") or (p_ch=="paper" and c_ch=="rock") or (p_ch=="scissors" and c_ch=="paper"):
        player_score += 1
        result = "Player win !"
    else:
        computer_score += 1
        result = "Computer win !"
    return (result, player_score, computer_score)

def actual_date():
    now = str(datetime.datetime.now())
    date = (now[:10])
    return date

def high_score(player_score, computer_score):
    result = ("Player score:", player_score, "    Computer score:", computer_score)
    result = formating(result)
    print(result)
    date = actual_date()
    to_file = (date +" :"+"      "+ result)
    with open("score.txt","w") as score:
        score.write(to_file)

def game(player_score, computer_score):
    try:
        player_choice = input("Enter your choice: ")
        if player_choice in choices:
                print("Player choice", player_choice)
                index = random.randint(0,2)
                computer_choice = choices[index]
                print("Computer choice:", computer_choice)
                result, player_score, computer_score = game_result(player_choice, computer_choice, player_score, computer_score)
                print(result)
                high_score(player_score, computer_score)
                game(player_score, computer_score)
        else:
            if player_choice == "x":
                print("Bye.")
                sys.exit(0)
            else:
                game(player_score, computer_score)
    except NameError:
        require()

def main():
    menu(choices)
    game(player_score, computer_score) 

main()
