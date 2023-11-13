package main

import "fmt"

//parameter k: a double that represents a temp in kelvin
//returns a double that is the calculated temp in celsius
func kelvinToCelsius(k float64) float64 {
	k = k - 273.15
	return k
}

func main() {
	fmt.Println("100 deg kelvin =", kelvinToCelsius(100))
}