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



