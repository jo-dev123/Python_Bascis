# Given a list [1,2,3,4], print out all the values in the list.
for num in [1,2,3,4]:
    print(num)

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
given_list = [1,2,3,4]
for num in given_list:
    print(num * 2)

# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
given_list = ["Elie", "Tim", "Matt"]
first_letter_list = []
for name in given_list:
    first_letter = first_letter_list.append(name[0])
print(first_letter_list)

# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
given_list = [1,2,3,4,5,6]
slice = given_list[1:6:2]
print(slice)

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
one_given_list = [1,2,3,4]
sec_given_list = [3,4,5,6]
new_list = [] 

for first_loop in one_given_list:
    if first_loop in sec_given_list:
        new_list.append(first_loop)

print(new_list)

# Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).
given_name_list = ["Elie", "Tim", "Matt"]
new_name_list = []

comp = [edit_name[::-1].lower()
for edit_name in given_name_list
]
print(comp) 

# Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).
first = "First"
third = "third"
new_string = []
first_in_arr = list(first)
third_in_arr = list(third)

comp = [common_letters for common_letters in first_in_arr if common_letters in third_in_arr]
new_string.extend(comp)

print(new_string)

# For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
range_1 = range(1,101)
for loop_through in range_1:
    if loop_through % 12 == 0:
        print(loop_through)

# Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
string_to_filter = "amazing"
vowels = ['a','e','i','o','u']
new_list =[]
for each_text in string_to_filter:
    if each_text not in vowels:
        new_list.append(each_text)
print(new_list)

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
gen_range = range(0,3)
comprehension = [[var for var in gen_range] for let in gen_range]
print(comprehension)

# Generate a list with the value:
gen_range = range(0,10)
comprehension2 = [[looper for looper in gen_range] for variable in gen_range]
print(comprehension2)