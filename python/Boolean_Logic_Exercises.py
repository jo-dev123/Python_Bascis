# Declare a variable called first and assign it to the value "Hello World".

first = "Hello World"

# Write a comment that says "This is a comment."
## This is a comment

# Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER")

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1<2<4:
    print("Math is fun")

# Assign a variable called nope to an absence of value.
nope = None

# Use the language's "and" boolean operator to combine the language's "true" value with its "false" value.
True and False

# Calculate the length of the string "What's my length?"
lenght_of_string = len("What's my length?")
print(lenght_of_string)

# Convert the string "i am shouting" to uppercase.
to_upper = "i am shouting".upper
print(to_upper)

# Convert the string "1000" to the number 1000.
to_num = int("1000")
print(to_num)
type(to_num)

# Combine the number 4 with the string "real" to produce "4real".
interpolation = str(4) + "real"
print(interpolation)

# Record the output of the expression 3 * "cool".
"""coolcoolcool"""

# Record the output of the expression 1 / 0.
"""ZeroDivisionError: division by zero"""

# Determine the type of [].
"""<class 'list'>"""

# Ask the user for their name, and store it in a variable called name.
name = input("What is your Name? ")

# Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.
str_num = input("Input any number? ")
any_num = int(str_num)
if any_num < 0:
    print("That number is less than 0!")
elif any_num > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# Find the index of "l" in "apple".
finding_l = "apple"
finding_l.find("l")

# Check whether "y" is in "xylophone".
finding_y = "xylophone"
finding_y.find("y")

# Check whether a string called my_string is all in lowercase.
my_string = "My string here is to the Glory of GOD"
print(my_string.islower())