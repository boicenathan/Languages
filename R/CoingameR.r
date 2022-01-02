
coingame <- function(gamenum, flips) {
    results <- round(runif(flips))

    heads <- sum(results == 0)
    tails <- sum(results == 1)

    return(toString(paste('Game ', gamenum, ' | Heads: ', format(heads, big.mark=","), 
    ' | Tails: ', format(tails, big.mark=","), ' | Total: ', format(heads + tails, big.mark=","))))
}

games <- 5
flips <- 1000000

for (x in 1:games) {
    print(coingame(x, flips))
}
