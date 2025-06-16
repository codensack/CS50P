def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha() or len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False
    alpha_before = True
    for ch in s:
        if alpha_before and ch == "0" or not alpha_before and ch.isalpha():
            return False
        if not ch.isalpha():
            alpha_before = False
    return True

main()