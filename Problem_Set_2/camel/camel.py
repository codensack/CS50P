name = input("camelCase: ")
for letter in name:
    if letter.isupper():
        print(f"{'_' + letter.lower()}", end='')
    else:
        print(letter)
print('')