import sys
import pyfiglet

def main():
    if len(sys.argv) == 1:
        font = None
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Bad usage")
        font = sys.argv[2]
        if font not in pyfiglet.FigletFont.getFonts():
            sys.exit("Font not found")
    else:
        sys.exit("Bad usage")

    text = input("Input: ")
    if font:
        fig = pyfiglet.Figlet(font=font)
    else:
        fig = pyfiglet.Figlet()
    print(fig.renderText(text))

if __name__ == "__main__":
    main()