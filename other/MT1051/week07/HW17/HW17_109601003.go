/*
Created Date: 2023/10/30
HW: 17
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func main() {
	// Define principal and interest rate
	principal := 42625.0
	interestRate := 0.0275 // 2.75% as a decimal

	// Initialize variables to track total interest and principal over time
	totalInterest := 0.0
	totalMoney := 0.0

	// Calculate and print interest and total amount for each year
	for year := 1; year <= 35; year++ {
		annualInterest := principal * interestRate
		totalInterest += annualInterest
		principal += annualInterest
		totalAmount := principal
		totalMoney += totalAmount
		fmt.Printf("Year %d: Interest: $%.2f Total Amount: $%.2f Total Money: $%.2f\n", year, annualInterest, totalAmount, totalMoney)
	}

	// fmt.Printf("Total Interest over 35 years: $%.2f\n", totalInterest)
}
