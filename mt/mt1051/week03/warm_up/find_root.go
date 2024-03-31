// Date: 2023/09/25
// Warm up
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
	"math"
)

func findRoots(a, b, c float64) interface{} {
	discriminant := b*b - 4*a*c

	if discriminant > 0 {
		root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		root2 := (-b - math.Sqrt(discriminant)) / (2 * a)
		return []float64{math.Round(root1*100) / 100, math.Round(root2*100) / 100}
	} else if discriminant == 0 {
		root1 := -b / (2 * a)
		return math.Round(root1*100) / 100
	} else {
		return "No real roots"
	}
}

func main() {
	var a, b, c float64
	fmt.Print("Enter the value of a: ")
	fmt.Scan(&a)
	fmt.Print("Enter the value of b: ")
	fmt.Scan(&b)
	fmt.Print("Enter the value of c: ")
	fmt.Scan(&c)

	roots := findRoots(a, b, c)

	switch r := roots.(type) {
	case []float64:
		fmt.Printf("The roots of the equation are %.2f and %.2f\n", r[0], r[1])
	case float64:
		fmt.Printf("The root of the equation is %.2f\n", r)
	case string:
		fmt.Println(r)
	}
}
