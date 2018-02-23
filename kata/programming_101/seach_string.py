# PRIMITIVE DATA TYPES
# str - string
# bool - boolean
# int - integer
# float

# COMPLEX DATA TYPES
# list
# dict

attendees = ['sara', 'alex', 'justin', 'ryan']

for attendee in attendees:
    # print(attendee)
    pass

# print(attendees[0])


# key = value
employees = {
    'sara': 'csa',
    'alex': 'it stupport tech',
    'justin': 'software ninja',
    'ryan': 'numbers nerd',
    'robot': str(1)
}

# print(employees['alex'])
# print(employees.get('ilya', 'russian spy'))

# for employee_id in employees:
#     print(employee_id + ' - ' + employees[employee_id])

# for key, value in employees.items():
#     print(key + ' - ' + value)


# CASTING
# str + int = runtime exception

# SCOPE
# white space in Python defines scope
#     block of code associated with a control structure

# def my_method():
#     temp = 1
# print(temp)

# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>

# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass

# -- exception handling --
# try <expression>:
#   <action>
# except [error_type]:
#   <handle error>

# try:
#     employees['iyla']
# except KeyError:
#     print('call alex to add access')
#     print('in exception')
# except Exception:
#     print('here')
# else:
#     print('else')

# --assignment--
# =

# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal


"""
  PRACTICE: print each letter in a given string
"""

name = 'justin'

# for char in name:
#     print(char)

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""


def print_char(input_name):
    for char in input_name:
        print(char)


# print_char(name)


"""
    PRACTICE: create a function that takes two inputs,
    then prints True/False whether or not the first input
    is contained within the second input
"""

text_value = 'some input'


def search_string(search_value, text_value):
    return search_value in text_value


print(search_string('a', text_value))  # False
print(search_string('s', text_value))  # True
print(search_string('S', text_value))  # False
