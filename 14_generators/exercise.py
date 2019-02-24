import types


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


# testing code
if isinstance(fib(), types.GeneratorType):
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
