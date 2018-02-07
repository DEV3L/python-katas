# DATA TYPES
# str - string
# bool - boolean
# int - integer
# float
# list

# CASTING
# str + int = runtime exception


# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>
#
# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass
#
# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal


text_value = 'some input'

"""
  PRACTICE: print each letter in a given string
"""

print('\n'.join(text_value))


"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""


def print_characters(input_string: str):
    print('\n'.join(input_string))


print_characters(text_value)


"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""


def search_string(search_value: str, input_string: str):
    print(search_value in input_string)


search_string('a', text_value)  # False
search_string('s', text_value)  # True
search_string('S', text_value)  # False
search_string('e i', text_value)  # True
