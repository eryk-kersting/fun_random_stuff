
import random


upper_limit = 1000
secret_number = random.randint(1,upper_limit)

count = 0
while (True):
    count = count + 1
    if (count > 7):
        print("You failed.")
        print ("The answer was", secret_number)
        break
    user_input = input("Guess my secret number (1 to {}): ".format(upper_limit))
    current_guess = int(user_input)
    if current_guess == secret_number:
        print("You got me!!")
        break
    elif current_guess < secret_number:
        print("Nope, it's bigger than that")
    else:
        print("Nope, it's less than that")


