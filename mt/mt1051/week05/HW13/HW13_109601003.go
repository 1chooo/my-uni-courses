/*
Created Date: 2023/10/16
HW: 13
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"time"
)

func main() {
	// Initial monthly salary and annual salary increase rate
	initialMonthlySalary := 48200.0  // Initial monthly salary
	annualSalaryIncrease := 0.035    // Annual salary increase rate (3.5%)

	// Number of years and months
	years := 25
	monthsPerYear := 12

	// Initial working date and month
	startDateStr := "2023-01-01"
	startDate, _ := time.Parse("2006-01-02", startDateStr)
	startYear := startDate.Year()

	// Initialize variables
	currentSalary := initialMonthlySalary
	totalIncome := 0.0

	// Calculate monthly salary and total income for the next 25 years
	for year := startYear; year < startYear+years; year++ {
		for month := 1; month <= monthsPerYear; month++ {
			// Calculate total income for the current month
			totalIncome += currentSalary

			// Print the monthly salary and total income for the current month
			fmt.Printf("%d-%02d: Monthly Salary: $%.2f\n", year, month, currentSalary)

			// Update the monthly salary (annual salary increase)
			currentSalary *= (1 + annualSalaryIncrease)
		}
		fmt.Printf("Year %d: Total Income: $%.2f\n", year, totalIncome)
	}

	// Print the total income after 25 years
	fmt.Printf("Total income after 25 years: $%.2f\n", totalIncome)
}
