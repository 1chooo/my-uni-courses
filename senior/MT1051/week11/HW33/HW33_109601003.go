/*
Created Date: 2023/12/04
HW: 33
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	// System of equations coefficients matrix
	coefficients := [4][4]float64{
		{2, 3, -4, 1},
		{1, -2, 3, -2},
		{3, 5, 1, -1},
		{4, 1, -1, 1},
	}

	// Constants vector
	constants := [4]float64{15, -3, 20, 5}

	// Gaussian elimination to solve the system of equations
	solution := gaussianElimination(coefficients, constants)

	fmt.Println("Solution:")
	fmt.Printf("x = %.0f, y = %.0f, z = %.0f, w = %.0f\n", math.Round(solution[0]), math.Round(solution[1]), math.Round(solution[2]), math.Round(solution[3]))

	// Numerical integration
	lowerLimit := math.Cos(0)
	upperLimit := math.Cos(math.Pi / 4)

	// Function to be integrated
	integrand := func(u float64) float64 {
		return math.Sqrt(1 + math.Cos(2*u))
	}

	// Perform numerical integration using the trapezoidal rule
	result := trapezoidalRule(integrand, lowerLimit, upperLimit)

	fmt.Println("数值积分的结果为:", result)
}

// Gaussian Elimination for solving system of linear equations
func gaussianElimination(coefficients [4][4]float64, constants [4]float64) [4]float64 {
	n := len(coefficients)

	for i := 0; i < n; i++ {
		// Find pivot for column i
		maxIndex := i
		for j := i + 1; j < n; j++ {
			if math.Abs(coefficients[j][i]) > math.Abs(coefficients[maxIndex][i]) {
				maxIndex = j
			}
		}

		// Swap rows
		coefficients[i], coefficients[maxIndex] = coefficients[maxIndex], coefficients[i]
		constants[i], constants[maxIndex] = constants[maxIndex], constants[i]

		// Make all rows below this one 0 in current column
		for j := i + 1; j < n; j++ {
			factor := coefficients[j][i] / coefficients[i][i]

			for k := i; k < n; k++ {
				coefficients[j][k] -= factor * coefficients[i][k]
			}
			constants[j] -= factor * constants[i]
		}
	}

	// Back substitution
	var solution [4]float64
	for i := n - 1; i >= 0; i-- {
		solution[i] = constants[i]
		for j := i + 1; j < n; j++ {
			solution[i] -= coefficients[i][j] * solution[j]
		}
		solution[i] /= coefficients[i][i]
	}

	return solution
}

// Numerical integration using the trapezoidal rule
func trapezoidalRule(f func(float64) float64, a, b float64) float64 {
	n := 1000 // Number of intervals
	h := (b - a) / float64(n)

	result := (f(a) + f(b)) / 2.0
	for i := 1; i < n; i++ {
		result += f(a+float64(i)*h)
	}
	result *= h

	return result
}
