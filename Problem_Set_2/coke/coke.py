p = 50
while (p > 0):
    print(f"Amount Due: {p}")
    c = int(input("Insert Coin: "))
    if c in [5, 10, 25]:
        p -= c
print(f"Change Owed: {p * -1}")