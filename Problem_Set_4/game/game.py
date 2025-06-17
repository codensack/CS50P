import random

play_game = True
while play_game:
    try:
        n = int(input("Level: "))
        if n < 0:
            continue 
        n = random.randint(1, n)
        while play_game:
            try:
                g = int(input("Guess: "))
            except ValueError:
                continue
            if g < n:
                print("Too small!")
            elif g > n:
                print("Too large!")
            else:
                print("Just right!")
                play_game = False
    except ValueError:
        pass