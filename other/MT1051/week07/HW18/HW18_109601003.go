/*
Created Date: 2023/10/30
HW: 18
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func funcValue(y float64) float64 {
	return (y + 3.2) * (y - 5.3) * (y + 2.7)
}

func main() {
	target := 1823.0
	lowerBound := 0.0
	upperBound := 20.0
	precision := 0.001

	for upperBound - lowerBound > precision {
		mid := (lowerBound + upperBound) / 2
		if funcValue(mid) < target {
			lowerBound = mid
		} else {
			upperBound = mid
		}
	}

	y := (lowerBound + upperBound) / 2

	if y > 12 {
		fmt.Println("y is greater than 12")
	} else if y < 12 {
		fmt.Println("y is less than 12")
	}
}
