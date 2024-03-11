// Date: 2023/09/25
// HW: 05
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
	"math"
)

func calculateProbability(x int, lambdaValue float64) float64 {
	eToTheMinusLambda := math.Exp(-lambdaValue)
	lambdaPowerX := math.Pow(lambdaValue, float64(x))
	factorialX := 1.0

	for i := 1; i <= x; i++ {
		factorialX *= float64(i)
	}

	probability := (eToTheMinusLambda * lambdaPowerX) / factorialX
	return probability
}

func main() {
	lambdaValue := 0.26

	for x := 1; x <= 6; x++ {
		probability := calculateProbability(x, lambdaValue)
		fmt.Printf("P(x=%d, lambda=%.2f) = %.6f\n", x, lambdaValue, probability)
	}
}
