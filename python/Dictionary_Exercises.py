# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
list = [("name", "Elie"), ("job", "Instructor")]
dictionary_list = {keys:values for (keys,values) in list}
print(dictionary_list)

# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dict_two_list = {list1[i]:list2[i] for i in range(0,len(list1))}
print(dict_two_list)

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = ["a","e","i","o","u"]
vowel_zero = {vowel:0 for vowel in vowels}
print(vowel_zero)

# Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. You should return something like this (Hint - use chr(65) to get the first letter):
all_letter = [chr(each_letter) for each_letter in range(65,91)]
num = [itr_num for itr_num in range(1,27) ]
count_letter = {num[i]:all_letter[i] for i in range(0,len(all_letter))}
print(count_letter)

"""Alternative {(count-64): chr(count) for count in range(65,91)}

# or 

{(count+1): chr(count+65) for count in range(0,26)}"""

