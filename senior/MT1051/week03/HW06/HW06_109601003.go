// Date: 2023/09/25
// HW: 06
// Author: 林群賀
// Student Number: 109601003

package main

import (
    "fmt"
    "math"
)

func normalDistribution(x float64, mu float64, a float64) float64 {
    coefficient := 1 / (a * math.Sqrt(2 * math.Pi))
    exponent := -0.5 * math.Pow((x - mu) / a, 2)
    return coefficient * math.Exp(exponent)
}

func main() {
    mu := 2.64
    a := 0.38

    xValues := []float64{0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5}

    for _, x := range xValues {
        pdf := normalDistribution(x, mu, a)
        fmt.Printf("x = %.2f: Normal Distribution = %.6f\n", x, pdf)
    }
}
