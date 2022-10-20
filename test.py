x = {"a": [1,1], "b": [1], "c": []}

y = sorted(x.items(), key=lambda a: len(a[1]))

print(dict(y))