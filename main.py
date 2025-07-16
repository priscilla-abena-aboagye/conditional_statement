import random
value = input("Enter a value (int or str): ")

match value:
    case int():
        print(f"You entered an integer: {value}")
    case str():
        print(f"You entered a string: {value}")
    case _:
        print("Inavlid data type")

age = input("Enter your age: ")
match age:
	case 18 | 19:
		if age >= 18 and has_id(user):
			print("You are eligible to vote")
		else:
			print("You need an id to vote")
	case _:
		print("You are not eligible to vote")

secret_number = random.randint(1, 10)
guess = int(input("Enter your guess: ")) 

match guess:
	case _ if guess == secret_number:
		print("Congratulations!. You guessed")
	case _ if guess > secret_number:
		print("Oops, your guess is a bit high. Try again!")
	case _ if guess < secret_number:
		print("Nope, your guess is a bit low. Give it another shot!")
	case _:
		print("That is an invalid guess")




