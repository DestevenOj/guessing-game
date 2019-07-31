#this game is using while loop to continually ask the user to guess correctly

secret_word = "antelope"
guess = " "

while guess != secret_word:
    guess = input("Enter guess:")
print("It was a correct guess!")

