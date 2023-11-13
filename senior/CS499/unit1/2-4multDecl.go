package main
import "fmt"
func main() {
	var (
		distance = 56000000
		speed = 100800
	)

	var dist2, speed2 = 56000000, 10800

	fmt.Println("There are 2 different ways to declare multiple variables at once.")
	fmt.Println("Grouping with parenthesis gets us values: distance =", distance, ", speed =", speed)
	fmt.Println("Weird same line syntax gets us values: dist2 =", dist2, ", speed2 =", speed2)
}