// Date: 2023/10/02
// HW: 10
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
)

type CalculateR struct {
	N int
}

func (c *CalculateR) calculate() float64 {
	R := 0.0
	for i := 2; i <= c.N; i++ {
		R += (1 - 1.0/float64(i))
	}
	return R
}

func main() {
	var N int
	fmt.Print("Enter a value for N: ")
	fmt.Scan(&N)

	calculator := CalculateR{N: N}
	result := calculator.calculate()
	fmt.Println(result)
}
