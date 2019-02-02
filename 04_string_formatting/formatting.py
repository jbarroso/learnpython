name = 'John'
print('Hello %s!' % name)
age = 41
print('%s is %d' % (name, age))
mylist = [1, 2, 3]
print('%s a list' % mylist)

# Arguments:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed
# amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

print('my %.3f dollars' % 3.333333)
