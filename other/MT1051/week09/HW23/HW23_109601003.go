/*
Created Date: 2023/11/20
HW: 23
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func countDepreciation() {
	initValue := 100000
	rate := 9000

	for i := 1; i <= 10; i++ {
		depreciationExpense := rate
		accumulatedDepreciation := rate * i
		endOfYearValue := initValue - rate*i

		fmt.Printf("Year %d, Depreciation expense: %d, Accumulated depreciation: %d, End of year value: %d\n", i, depreciationExpense, accumulatedDepreciation, endOfYearValue)
	}
}

func main() {
	countDepreciation()
}
