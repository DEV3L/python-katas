# DATA TYPES

# str - string
_str = 'test'
_str2 = "tst"
_str3 = '{_str2} test'.format(_str2=_str2)
_str4 = f'{_str} test'

# bool - boolean
_bool = True
_bool_false = False

# int - integer
_int = 1
_int_negative = -1

# float
_float = 1.0
_float_negative = -1.0

# list

_list = ['alex', 'grande', 'sara',
         'danie', 'laura', 'jen']

for name in _list:
    print(name)

_list2 = list()

# CASTING

output = float('1.0') + 1
output2 = '1' + str(1)

print(output)
print(output2)

print(bool(0))
print(bool(1))
print(bool(.1))
print('---')

print(len(''))
print(len('false'))

print(bool(''))
print(bool('false'))
print(bool(None))
print(bool([]))

"""
  practice: print each letter in a given string
"""

# for {variable_name} in <collection>:
#     <action>
name = 'name'
for character in name:
    print(character)

"""
  practice: create a function that takes an input,
  then prints each character of the input
"""


def print_character(input):
    for character in input:
        print(character)


print_character('supercalifragilisticexpealidocious')

"""
    practice: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""


# == compares
def search_character(search, find):
    is_found = False
    for character in find:
        if character == search:
            is_found = True

    print(is_found)


search_character('a', 'purple')
