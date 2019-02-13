import re

fns = dir(re)
result = []

for fn in fns:
    if "find" in fn:
        result.append(fn)
print(result)

# functional way:
print(list(filter(lambda fn: "find" in fn, fns)))
