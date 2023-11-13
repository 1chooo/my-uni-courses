//for printf
// - pads the right
// non negative pads the left
package main

import (
	"fmt"
)
func main() {
	fmt.Println("Using printf")
	fmt.Printf("My weight on the surface of Mars is %v lbs,", 149.0*0.3783)
	fmt.Printf(" and I would be %v years old.\n", 41*365/687)
	fmt.Print("\nnow testing printf with pretty spacing\n")
	fmt.Printf("%-25v $%-4v\n", "Reed Ring Space Program", 420)
	fmt.Printf("%-25v $%-4v\n", "Virgin Galactic", 100)
}