// Simulate a large number of coin flips using JavaScript
function coingame(flips, gamenum) {
    // Declare the variables
    let heads = 0;
    let tails = 0;
    let i = 0;
    let toss = 0;

    // Start the loop
    for (i; i < flips; i++) {
        toss = Math.round(Math.random());
        if (toss == 0) {
            heads++;
        } else {
            tails++;
        }
    }
    // Return the results
    return `Game: ${gamenum + 1} | Heads: ${heads.toLocaleString()} | Tails ${(tails.toLocaleString())} | Total: ${(heads + tails).toLocaleString()}`
}

// Call the function with the number of games and flips
let i = 0;
let games = 5;
let flips = 1000000;
console.log("< JavaScript >");
for (i; i < games; i++) {
    console.log(coingame(flips, i));
}
