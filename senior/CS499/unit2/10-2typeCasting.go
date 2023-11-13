package main

import "fmt"

func main() {
	var age int = 41
	var marsAge = float64(age)

	var marsDays = 687.0
	var earthDays = 365.2425
	marsAge = marsAge * earthDays / marsDays
	fmt.Println("I am", marsAge, "years old on mars.")
}