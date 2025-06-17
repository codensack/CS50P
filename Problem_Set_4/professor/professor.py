import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        result = a + b

        tries = 0
        while tries < 3:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1
        print(f"{a} + {b} = {result}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()