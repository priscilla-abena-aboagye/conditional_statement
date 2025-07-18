'''
import random
value = input("Enter a value (integer or string): ")

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
# Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
# Initialize a variable total to 0, which will store the running sum.
# Use a for loop to iterate over the numbers list.
# Inside the loop, add the current number (use the loop variable) to the total variable.
# After the loop, print the final total value, which represents the sum of all the numbers in the list.
'''

sum = 0

for number in range(1, 11):
	sum += number
print(f"The sum of all the numbers is {sum}")

# Guessing game 
guess_count = 0
selected_number = random.randint(1, 20)
user_guess = 0

while user_guess != selected_number:
	guess_count += 1
	user_guess = int(input("Enter a number between 1 and 20: "))
	if user_guess > selected_number:
		print("Too high!.")
	elif user_guess < selected_number:
		print("Too Low!.")
print(f"Congratulations! You guessed the number in {guess_count} attempts.")

# Counting down 
outer_counter = 5

while outer_counter > 0:
	inner_counter = 1
	while inner_counter <= outer_counter:
		print(inner_counter, end="")
		inner_counter += 1
	outer_counter -= 1 

# multiplication table
print("=====MULTIPLICATION TABLE=====\n")
for number in range(1, 13):
	for i in range(1, 13): # 2 X 1 = 2
		product = i * number
		print(f"{i} X {number} = {product:2}", end="\t")
	print()


# Triangle
rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks

a = [1, 2, 3]
b = [4, 5, 6]
for i in a:
	for x in b:
		print(i, x)

i = 0

while i < len(a):
    j = 0
    while j < len(b):
        print(a[i], b[j])
        j += 1
    i += 1
'''
# Pyramid
rows = 5

while rows > 0:
	columns = 0
	while columns < rows:
		multiple = "*" * columns 
		print(multiple)
		columns += 1
	rows -= 1