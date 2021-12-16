package main
import("math/rand"
	   "fmt")

func main() {
	// Declare the number of games and flips per game
	var games, flips int = 5, 1000000
	// Start the games
	fmt.Printf("< Go >\n")
	for i:=0; i < games; i++ {
		coingame(flips, i)
	}
}

func coingame(flips int, i int) {
	var heads, tails, toss int = 0, 0, 0
	// Start flipping the 'coin'
	for i:=0; i < flips; i++ {
		toss = rand.Intn(2)
		if toss == 0 {
			heads++
		} else {
			tails++
		}
	}
	// Return the results
    fmt.Printf("Game %d | Heads: %d | Tails: %d | Total: %d\n", i + 1, heads, tails, heads + tails)
}