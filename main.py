import random

def get_guess():
    while True:
        try:
            user_input = input("Enter 4 numbers as guesses: ")
            user_list = []
            for item in user_input:
                user_list.append(int(item))
            illegal_num = False
            illegal_num2 = False
            illegal_length = False
            for number in user_list:
                if number > 7 or number < 1:
                        illegal_num = True
                if user_list.count(number) > 1:
                    illegal_num2 = True
            if len(user_list) != 4:
                illegal_length = True
            if illegal_length:
                print("Your guess must consist of 4 numbers!")
            if illegal_num:
                print("You can only use numbers 1-7 as guesses!")
            if illegal_num2:
                print("You can only use each number once")
            if not illegal_num and not illegal_num2 and not illegal_length:
                return user_list
        except ValueError:
            print("You need to input the numbers without spaces as such: 1234")
print (get_guess())


def check_values(num_array, guesses):
    response = []
    for number in num_array:
        if number in guesses:
            if num_array.index(number) == guesses.index(number):
                response.append("RED")
            else:
                response.append("WHITE")
        random.shuffle(response)
        print(response)
        return (check_win(response))



def check_win(response_list):
    win=0
    for guess in response_list:
        if guess == "RED":
            win = win+1
        if win == 4:
            print("Congrats! You got it!!")
        return win

def create_comp_list():
    game_list=[]
    while len(game_list) < 4:
        random_num = random.randint(1,7)
        if random_num not in game_list:
            game_list.append(random_num)
    return game_list




def play_game():
    game_list = create_comp_list()
    total_guesses=0
    while total_guesses<5:
        print("Guesses remaining: " + str(5-total_guesses))
        user_input = get_guess()
        if check_values(game_list,user_input) == 4:
            break
        total_guesses = total_guesses+1
    if total_guesses == 5:
        print("Sorry! That's all the guesses you get!")
        print("This is the corect answer:")
        print(game_list)
    print("Thanks for playing!")



# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.



play_game()