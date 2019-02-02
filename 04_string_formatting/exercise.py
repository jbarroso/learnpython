# data is a tuple object
data = ("John", "Doe", 53.44)
format_string = "Hello"

# Hello John Doe. Your current balance is $53.44.
print(
    '%s %s %s. Your current balance is $%f.'
    % (format_string, data[0], data[1], data[2])
)

# with only a tuple:
print(
    '%s %s %s. Your current balance is $%f.'
    % ((format_string,) + data)
)
