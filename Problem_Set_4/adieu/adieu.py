import sys

def main():
    names = []
    try:
        while True:
            names.append(input("Name: "))
    except (EOFError, KeyboardInterrupt):
        pass

    print("Adieu, adieu, to " + format_names(names))

def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return ", ".join(names[:-1]) + f", and {names[-1]}"

if __name__ == "__main__":
    main()