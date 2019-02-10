astring = "Hello_world!"
print("single quotes are ' '")

# Length
print(len(astring))

# index of
print(astring.index("o"))

# number of chars
print(astring.count("l"))

# slice of string (starting at index 3, and ending at index 6)
print(astring[3:7])
print(astring[3:7:1])  # skiping 1 (step=1) is the same

# slice of string (starting at index 3, and ending at index 6)
# skiping 2 caracteres (step=2)
print(astring[3:7:2])
print(astring[3::2])

# reverse string (negative step)
print(astring[::-1])

# common operations:
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split("_")
print(afewwords)
