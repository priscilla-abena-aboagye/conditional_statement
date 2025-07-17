import random
value = input("Enter a value (int or str): ")

match value:
    case int():
        print(f"You entered an integer: {value}")
    case str():
        print(f"You entered a string: {value}")
    case _:
        print("Inavlid data type")

age = int(input("Enter your age: "))
match age:
	case _ if age >= 18:
		print("You are eligible to vote")
	case _:
		print("You are not eligible to vote")

secret_number = random.randint(1, 10)
guess = int(input("Enter a random number between 1 to 10: ")) 

match guess:
	case _ if guess == secret_number:
		print("Congratulations!. You guessed")
	case _ if guess > secret_number:
		print("Oops, your guess is a bit high. Try again!")
	case _ if guess < secret_number:
		print("Nope, your guess is a bit low. Give it another shot!")
	case _:
		print("That is an invalid guess")


'''
Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
Initialize a variable total to 0, which will store the running sum.
Use a for loop to iterate over the numbers list.
Inside the loop, add the current number (use the loop variable) to the total variable.
After the loop, print the final total value, which represents the sum of all the numbers in the list.
'''

list_of_numbers = [1, 2, 3, 4, 5]
sum = 0
for number in list_of_numbers:
	sum += number
print(f"The sum of all the numbers is {sum}")

