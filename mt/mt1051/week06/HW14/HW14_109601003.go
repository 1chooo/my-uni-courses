/*
Created Date: 2023/10/23
HW: 14
Author: 林群賀
Student Number: 109601003
*/

package main

import (
    "fmt"
)

func main() {
    // Initial monthly salary and annual salary increase rate
    initialMonthlySalary := 48200  // Initial monthly salary
    annualSalaryIncrease := 0.035  // Annual salary increase rate (3.5%)

    // Desired salary thresholds
    desiredMonthlySalary := 115000  // Desired monthly salary
    desiredAnnualSalary := 1025000  // Desired annual salary

    // Number of years and months
    years := 25
    monthsPerYear := 12

    // Initial working date and month
    startYear := 2023

    // Initialize variables
    currentSalary := float64(initialMonthlySalary)
    totalIncome := 0.0
    yearsToReachMonthlyGoal := 0
    yearsToReachAnnualGoal := 0

    // Calculate monthly salary and total income for the next 25 years using a for loop
    for year := startYear; year < startYear+years; year++ {
        for month := 1; month <= monthsPerYear; month++ {
            // Calculate total income for the current month
            totalIncome += currentSalary
            // Check if monthly salary exceeds the desired monthly salary
            if currentSalary >= float64(desiredMonthlySalary) && yearsToReachMonthlyGoal == 0 {
                yearsToReachMonthlyGoal = year
                fmt.Printf("Monthly Salary Exceeds $115,000 in %d-%02d\n", year, month)
            }
            // Update the monthly salary (annual salary increase)
            currentSalary *= (1 + annualSalaryIncrease)
        }

        if totalIncome >= float64(desiredAnnualSalary) && yearsToReachAnnualGoal == 0 {
            yearsToReachAnnualGoal = year
            fmt.Printf("Annual Salary Exceeds $1,025,000 in Year %d\n", year)
        }

        if yearsToReachMonthlyGoal != 0 && yearsToReachAnnualGoal != 0 {
            break
        }
    }

    // Print the total income after 25 years
    fmt.Printf("Total income after 25 years: $%.2f\n", totalIncome)
}
