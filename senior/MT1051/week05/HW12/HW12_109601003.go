/*
Created Date: 2023/10/16
HW: 12
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func targetFunction1(x float64) float64 {
	return 3 * x * x - 6 * x + 3
}

func findMin1(startX, endX, step float64) (float64, float64) {
	minX := startX
	minY := targetFunction1(startX)

	currentX := startX

	for currentX <= endX {
		currentY := targetFunction1(currentX)
		if currentY < minY {
			minX = currentX
			minY = currentY
		}
		currentX += step
	}

	return minX, minY
}

func targetFunction2(x float64) float64 {
	return 0.5*x*x - 3*x + 7.5
}

func findMin2(startX, endX, step float64) (float64, float64) {
	minX := startX
	minY := targetFunction2(startX)

	currentX := startX

	for currentX <= endX {
		currentY := targetFunction2(currentX)
		if currentY < minY {
			minX = currentX
			minY = currentY
		}
		currentX += step
	}

	return minX, minY
}

func main() {
	startX := -10.0
	endX := 10.0
	step := 0.01

	minX1, minY1 := findMin1(startX, endX, step)
	minX2, minY2 := findMin2(startX, endX, step)

	fmt.Printf("(1) min: x = %f, y = %f\n", minX1, minY1)
	fmt.Printf("(2) min: x = %f, y = %f\n", minX2, minY2)
}
