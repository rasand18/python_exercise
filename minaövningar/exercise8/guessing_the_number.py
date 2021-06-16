

input_n = int(input("Enter a number: "))
print('\033[H\033[J', end='')
input_n2 = int(input("How many guesses do you want?: "))
print('\033[H\033[J', end='')
guess = 0


while guess < input_n2 or input_n2 == 1:
    guesses = int(input("Guess the number: "))
    if guesses == input_n:
        print("You picked the right number")
        break
    else:
        print(f"Wrong, you have {input_n2 - 1} tries left")
        input_n2 = input_n2-1
        if input_n2 == 0:
            print("You have no guesses left")

