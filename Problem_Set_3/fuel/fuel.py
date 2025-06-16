while True:
    try:
        a, b = input("Fraction: ").split('/')
        p = round(int(a) / int(b) * 100)
        if p <= 1:
            print("E")
        elif p > 100:
            raise ValueError
        elif p >= 99:
            print("F")
        else:
            print(f"{p}%")
        break
    except (ValueError, ZeroDivisionError):
        pass