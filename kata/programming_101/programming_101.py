# lines that start with '#' are a comment
# multiple line comments start and end with three double quotes

"""
multiline comment
"""

# in PyCharm, right click and select run 'programming_101' to execute

print('Hello, world!')

# -----------------
#  PRIMITIVE DATA TYPES
# -----------------
"""
  str - string
  'hello world'

  PRACTICE: Print a string to the console
"""

"""
  bool - boolean
  True/False

  PRACTICE: Print a boolean value to the console
"""

"""
  int - integer
  0

  PRACTICE: Print a string to the console
"""

"""
  float - decimal
  0.0

  PRACTICE: Print a float to the console
"""

# -----------------
# COMPLEX DATA TYPES
# -----------------

"""
  list
  [], ['word']

  PRACTICE: Create a list that contains the names of three people
"""

"""
  dict
  {}, {'key', 'value}

  PRACTICE: Create a dictionary that is name as a key and gender as the value
"""

# -----------------
# CASTING
# -----------------
"""
  data types can be forced from one type to another under certain conditions
    str()
    bool()
    float()
    int()
  
  PRACTICE: 1. Add the string of '1' to the int of 1 to output the string '11'
            2. Add the int of 1 to the string of '1' to output the int 2
            3. Cast an empty string value to a boolean to output False
            4. Cast any non-empty string value to a boolean to output True
            5. Cast the result of 3/2 to a float values to produce an output of 1.5
"""

# -----------------
# SCOPE
# -----------------
# white space in Python defines scope
#     block of code associated with a control structure

# -----------------
# CONTROL STRUCTURES
# -----------------
"""
-- variable assignment --
  =
  my_variable = 'value'
  
  PRACTICE: Create a variable with a name of your choosing that contains the value 'hello'
"""

"""
-- logical --
  if <bool>:
    <action>
  elif <bool>:
    <action>
  else <bool>:
    <action>
    
  PRACTICE: Write an if check to see if a value is equal to 'hello world', 
                if true print 'hello', else print 'bye'
"""

"""
-- exception handling --
  try <expression>:
    <action>
  except [error_type]:
    <handle error>
  
  PRACTICE: In a try block, divide 1 by 0, except a ZeroDivisionError and print 'zero divison error' 
"""

"""
-- while loops --
  while <bool>:
    <action>

  PRACTICE: 
"""

# --for loops--
# for {variable_name} in <collection>:
#     <action>


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
