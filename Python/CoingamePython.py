### Simulate a large number of coin flips using Python ###
from random import randint


def coingame(flips: int, gamenum: int):
    """ Function to simulate specified number of coin flips and prints the results.
    Args:
        flips (int): Number of flips.
    """
    heads = tails = 0
    for _ in range(0, flips):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
        
    # Printing the results and showing the distribution with a pie graph
    print(f"Game {gamenum + 1} | Heads: {heads:,} | Tails: {tails:,} | Total: {heads + tails:,}") 

    
if __name__ == '__main__':
    # Call the function with the number of games and flips
    games = 5
    flips = 1000000
    print("< Python >")
    for i in range(0, games):
        coingame(flips, i)
    