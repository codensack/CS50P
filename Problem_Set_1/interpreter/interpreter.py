term = input("Expresseion: ").split()
if term[1] == '*':
    print(f"{(float(term[0]) * float(term[2])):.1f}")
elif term[1] == '/':
    print(f"{(float(term[0]) / float(term[2])):.1f}")
elif term[1] == '+':
    print(f"{(float(term[0]) + float(term[2])):.1f}")
elif term[1] == '-':
    print(f"{(float(term[0]) - float(term[2])):.1f}")