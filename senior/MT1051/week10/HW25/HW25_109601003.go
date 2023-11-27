/*
Created Date: 2023/11/27
HW: 25
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func compoundInterest(principal float64, rate float64, years int) ([]float64, []float64) {
	principals := []float64{principal} // Slice to store principal amounts
	compound := []float64{principal}   // Initial principal for year 0

	for year := 1; year <= years; year++ {
		principal += principal * rate // Update principal to include interest
		compound = append(compound, principal)
		principals = append(principals, compound[year-1])
	}

	return principals, compound
}

func main() {
	initialPrincipal := 33500.0     // Initial principal
	annualInterestRate := 0.0225    // Annual interest rate
	investmentYears := 25           // Investment period

	principals, result := compoundInterest(initialPrincipal, annualInterestRate, investmentYears)

	for i := 0; i < len(result); i++ {
		fmt.Printf("第 %d 年本金: $%.2f 期末本利和: $%.2f\n", i, principals[i], result[i])
	}
}
