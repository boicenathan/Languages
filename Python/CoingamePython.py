### Simulate a large number of coin flips using Python ###
from random import randint


def coingame(numflips: int, gamenum: int):
    flips = []
    for _ in range(0, numflips):
        flips.append(randint(0, 1))
    heads = flips.count(0)
    tails = flips.count(1)
    # Printing the results and showing the distribution with a pie graph
    print(f"Game {gamenum + 1} | Heads: {heads:,} | Tails: {tails:,} | Total: {heads + tails:,}") 

    
if __name__ == '__main__':
    # Call the function with the number of games and flips
    games = 5
    flips = 1000000
    print("< Python >")
    for i in range(0, games):
        coingame(flips, i)
    