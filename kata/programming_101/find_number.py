import sys

_messsage = sys.argv[0]

_str = "this is a str"
_str_2 = 'this is a str'

_bool = True  # False
_int = 1
_float = 1.0

# message = 'hello world'
#
# print(message)


"""
  practice: print each letter in a given string
"""

message = "programming 101"

# brute force
print('p')
print('r')
print('o')
print('g')
print('r')
print('a')
print('m')
print('m')
print('i')
print('n')
print('g')
print(' ')
print('1')
print('0')
print('1')

print('-----')

# for {variable_name} in <collection>:
#     <action>

for letter in message:
    print(letter)

counts = [1, 2, 3, 4, 5, 6, 7, 8]

for count in counts:
    print(count)

"""
  practice: print true or false if a letter exists in a given str
"""

# search_value = 'e'
message = 'hello world'


def find_letter(search_value):
    if search_value in message:
        print(True)
    else:
        print(False)


find_letter('e')
find_letter('a')
find_letter('z')
# find_letter(1)
find_letter('y')
find_letter('l')
# p
# r
# o
# g
# r
