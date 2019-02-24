# edit the functions prototype and implementation
def foo(a, b, c, *rest):
    return len(rest)


def bar(a, b, c, **options):
    return options.get('magicnumber') == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) is False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) is True:
    print("Awesome!")
