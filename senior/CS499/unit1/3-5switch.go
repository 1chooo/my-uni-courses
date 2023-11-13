package main

import "fmt"

func main() {
	var command = "play fortnite"

	switch command {
	case "play fortnite":
		fmt.Println("you get deku smashed")
	case "play minecraft":
		fmt.Println("you mine straight down and die in lava")
	default:
		fmt.Println("Invalid switch expression")
	}
}