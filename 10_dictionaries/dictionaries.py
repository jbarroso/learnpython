# Definition:
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Other notation:
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook)

# Iterating
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Delete an element
del phonebook["John"]
print(phonebook)

# Pop an element
jack_number = phonebook.pop("Jack")
print(jack_number)

print(phonebook)
