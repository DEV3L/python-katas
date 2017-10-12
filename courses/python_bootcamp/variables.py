# Strings
single_quote = 'single_quote'
double_quotes = "double_quotes"
escape_character = '\''

# Numbers
integer = 0
double = 0.0
complex = 0j

# Truthiness
False
True
bool(None)  # False
bool(0)  # False
bool('')  # False
bool(())  # False
bool([])  # False

# zero of any numeric type, for example, 0, 0L, 0.0, 0j.
#
# any empty sequence, for example, '', (), [].
#
# any empty mapping, for example, {}.
#
# instances of user-defined classes, if the class defines a __nonzero__() or __len__() method, when that method returns the integer zero or bool value False. [1]
#
#
