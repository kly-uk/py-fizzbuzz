# Fizzbuzz - Create children's game
# Based on a traditional English children's game
# Print the numbers 1..100
# For multiples of 3, print "Fizz" instead of the number
# For multiples of 5, print "Buzz" instead of the number
# For multiples of 3 and 5, print "FizzBuzz" instead of the number

from math import floor, ceil

# There are 4 different methods so far. Uncomment the function in main() to test!

def main():
	methodOne()
	#methodTwo()
	#methodThree()
	#methodFour()

def methodOne():
	for number in range(1, 101):
		if number % 15 == 0:
			print("FizzBuzz")
		elif number % 3 == 0:
			print("Fizz")
		elif number % 5 == 0:
			print("Buzz")
		else:
			print(number)

def methodTwo():
	for number in range(1, 101):
		if number % 3 == 0:
			if number % 5 == 0:
				print("FizzBuzz")
			else:
				print("Fizz")
		elif number % 5 == 0:
			print("Buzz")
		else:
			print(number)

def methodThree():
	fizzbuzz = {"3": "Fizz", "5": "Buzz"}
	for number in range(1, 101):
		output = ""
		for i in fizzbuzz:
			if number % int(i) == 0:
				output = output + fizzbuzz[i]
			elif i == "5" and output == "":
				output = number
		print(output)

def methodFour():
	for number in range(1, 101):
		output = ""
		if number / 3 == (floor(number / 3) or ceil(number /  3)): output = "Fizz"
		if number / 5 == (floor(number / 5) or ceil(number /  5)): output = output + "Buzz"
		if output == "": output = number
		print(output)


if __name__ == "__main__":
	main()
