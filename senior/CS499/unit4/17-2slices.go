package main 

import "fmt"

func main() {
	//slices are different datatypes then arrays and are used quite a bit instead
	//of arrays as function parameters
	dwarfArray := [...]string{"Ceres", "Pluto", "Haumea", "Makemake", "Eris"}
	dwarfSlice := dwarfArray[:]
}