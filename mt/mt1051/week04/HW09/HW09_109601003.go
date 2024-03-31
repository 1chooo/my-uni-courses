// Date: 2023/10/02
// HW: 09
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
)

type FunctionCalculator struct{}

func (f *FunctionCalculator) f(x float64) float64 {
	return 4.6 * x * x - 6.5 * x + 13.4
}

func (f *FunctionCalculator) calculateAndPrint(start, end int) {
	for i := start; i <= end; i++ {
		x := float64(i) + 0.4
		result := f.f(x)
		fmt.Printf("f(%.1f) = %.2f\n", x, result)
	}
}

func main() {
	calculator := FunctionCalculator{}
	calculator.calculateAndPrint(9, 20)
}

