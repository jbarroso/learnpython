x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

x = 3
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# A statement is evaulated as true if one of the following is
# correct:
# 1. The "True" boolean variable is given, or calculated using
# an expression, such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.
#
# Here are some examples for objects which are considered
# as empty:
# 1. An empty string: ""
# 2. An empty list: []
# 3. The number zero: 0
# 4. The false boolean variable: False

if "" or [] or 0 or False:
    print("Empty values are true!")
else:
    print("Empty values are false!")

# is operator compare the instances
x = ['foo']
y = ['foo']
print(x == y)  # Prints out True
print(x is y)  # Prints out False (with string and numbers is not true

# is operators with strings
# instead of wasting memory by creating two string objects,
# all interned strings with the same contents point to the
# same memory. This results in the Python "is" operator
# returning True because two strings with the same contents
# are pointing at the same string object.
x = 'foo'
y = 'foo'
print(x == y)  # Prints out True
print(x is y)  # Prints out True

# not
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False
