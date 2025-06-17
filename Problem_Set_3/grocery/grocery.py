def main():
    grocery_list = {}


    try:
        while True:
            item = input().strip()
            if not item:
                continue
            item_upper = item.upper()
            if item_upper in grocery_list:
                grocery_list[item_upper] += 1
            else:
                grocery_list[item_upper] = 1
    except EOFError:
            pass
    finally:
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()