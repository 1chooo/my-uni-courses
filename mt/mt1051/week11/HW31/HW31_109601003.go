/*
Created Date: 2023/12/04
HW: 31
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func main() {
	// Coefficients of the equations
	coefficients := [2][2]float64{{1, 4}, {5, -1}}
	constants := [2]float64{-1, 16}

	// Calculate the determinant of the coefficients matrix
	determinant := coefficients[0][0]*coefficients[1][1] - coefficients[0][1]*coefficients[1][0]

	// Check if the determinant is zero
	if determinant == 0 {
		fmt.Println("The system of equations has no unique solution")
		return
	}

	// Calculate the inverse of the coefficients matrix
	coefficientsInverse := [2][2]float64{
		{coefficients[1][1] / determinant, -coefficients[0][1] / determinant},
		{-coefficients[1][0] / determinant, coefficients[0][0] / determinant},
	}

	// Calculate the solution by multiplying the inverse of coefficients with constants
	var solution [2]float64
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			solution[i] += coefficientsInverse[i][j] * constants[j]
		}
	}

	fmt.Printf("Solution: X = %.4f, Y = %.4f\n", solution[0], solution[1])
}
