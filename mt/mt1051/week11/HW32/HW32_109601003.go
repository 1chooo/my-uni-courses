/*
Created Date: 2023/12/04
HW: 32
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("x^2 - 12x + 3 = 0")
	// 方程式的係數
	a := 2.0
	b := -12.0
	c := 3.0

	// 計算判別式
	discriminant := b*b - 4*a*c

	// 計算根
	if discriminant > 0 {
		// 有兩個實根
		root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		root2 := (-b - math.Sqrt(discriminant)) / (2 * a)
		fmt.Println("兩個實根：")
		fmt.Printf("根1 = %.4f, 根2 = %.4f\n", root1, root2)
	} else if discriminant == 0 {
		// 有一個重根
		root := -b / (2 * a)
		fmt.Println("一個重根：")
		fmt.Printf("根 = %.4f\n", root)
	} else {
		// 虛數根
		realPart := -b / (2 * a)
		imaginaryPart := math.Sqrt(math.Abs(discriminant)) / (2 * a)
		fmt.Println("兩個虛數根：")
		fmt.Printf("根1 = %.4f + %.4fi, 根2 = %.4f - %.4fi\n", realPart, imaginaryPart, realPart, imaginaryPart)
	}

	fmt.Println("-1/3x^2 + 4/9x - 4/27 = 0")
	// 方程式的係數
	a = -1.0 / 3
	b = 4.0 / 9
	c = -4.0 / 27

	// 計算判別式
	discriminant = b*b - 4*a*c

	// 計算根
	if discriminant > 0 {
		// 有兩個實根
		root1 := (-b + math.Sqrt(discriminant)) / (2 * a)
		root2 := (-b - math.Sqrt(discriminant)) / (2 * a)
		fmt.Println("兩個實根：")
		fmt.Printf("根1 = %.4f, 根2 = %.4f\n", root1, root2)
	} else if discriminant == 0 {
		// 有一個重根
		root := -b / (2 * a)
		fmt.Println("一個重根：")
		fmt.Printf("根 = %.4f\n", root)
	} else {
		// 虛數根
		realPart := -b / (2 * a)
		imaginaryPart := math.Sqrt(math.Abs(discriminant)) / (2 * a)
		fmt.Println("兩個虛數根：")
		fmt.Printf("根1 = %.4f + %.4fi, 根2 = %.4f - %.4fi\n", realPart, imaginaryPart, realPart, imaginaryPart)
	}
}
