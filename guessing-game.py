#this game is using while loop to continually ask the user to guess correctly

secret_word = "antelope"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True
print("you failed!")

    

