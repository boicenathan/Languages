#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int coingame(int flips, int gamenum);

int main() {
    // Declare the number of games and flips per game
    int flips = 1000000, games = 5, n = 1;
    srand(time(NULL));

    // Start the games
    printf("C\n");
    for (n; n <= games; n += 1) {
        coingame(flips, n);
    }

    return 0;
}

int coingame(int flips, int gamenum) {
    int heads = 0, tails = 0, toss = 0, n, total = 0;

    // Start flipping the 'coin'
    for (n = 1; n <= flips; n += 1) {
        toss = rand() % 2;
        if (toss == 0) {
            heads++;
        } else {
            tails++;
        }
    }
    // Return the results
    printf("Game %d | Heads: %d | Tails: %d | Total: %d\n", gamenum, heads, tails, heads + tails);
}