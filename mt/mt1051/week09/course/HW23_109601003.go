/*
Created Date: 2023/11/20
HW: 22
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func f(x float64) float64 {
	return 6.5*x*x - 7.3*x + 2.7
}

func main() {
	for i := 11; i <= 20; i++ {
		num := float64(i) + 0.5
		result := f(num)
		fmt.Printf("x = %.1f, f(x) = %.2f\n", num, result)
	}
}

