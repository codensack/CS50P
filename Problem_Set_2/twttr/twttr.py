s = input("Input ")
for c in s:
    if c in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        continue
    print(c, end='')
print("")