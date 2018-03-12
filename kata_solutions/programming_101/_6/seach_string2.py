# PRIMITIVE DATA TYPES
# str - string
# bool - boolean
# int - integer
# float

# COMPLEX DATA TYPES
# list
# dict

# CASTING
# str + int = runtime exception

# SCOPE
# white space in Python defines scope
#     block of code associated with a control structure

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

# --assignment--
# =

# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal


# dunder score methods

# __add__ works on the + operator
# __eq__ works the == operator
# __str__ works the str operation
# __init__ the method that gets when a new instance is created ()

class Adventurer:
    def __init__(self, name):
        self.name = name

    def equals(self, other):
        return self.name == other.name

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return self.name + ' ' + other.name

    def __str__(self):
        return self.name + ' is an awesome person'


sara1 = Adventurer('sara')
sara2 = Adventurer('sarah')

print(sara1 == sara2)
print(sara1.equals(sara2))

print(sara1)
print(sara2)

sara3 = sara1
sara4 = sara1 + sara2
print(sara4)
print(sara1 is sara3)

"""
  PRACTICE: print each letter in a given string
"""

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""

"""
  PRACTICE: create a function that takes two inputs,
  then prints True/False whether or not the first input
  is contained within the second input
"""

# print(search_string('a', text_value))  # False
# print(search_string('s', text_value))  # True
# print(search_string('S', text_value))  # False


"""
  PRACTICE: Create a diction that contains a list of 
  employee titles stored by the name, then print each record 
  such that each employee name and title is printed on a line
"""
