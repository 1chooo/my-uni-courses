/*
Created Date: 2023/11/27
HW: 26
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func addMatrices(A, B [][]int) [][]int {
	rowsA := len(A)
	colsA := len(A[0])

	result := make([][]int, rowsA)
	for i := range result {
		result[i] = make([]int, colsA)
	}

	for i := 0; i < rowsA; i++ {
		for j := 0; j < colsA; j++ {
			result[i][j] = A[i][j] + B[i][j]
		}
	}

	return result
}

func main() {
	A := [][]int{
		{25, 32, 18},
		{16, 22, 54},
		{31, 29, 8},
		{25, 14, 65},
	}

	B := [][]int{
		{14, 24, 7},
		{52, 32, 13},
		{33, 24, 55},
		{72, 81, 29},
	}

	result := addMatrices(A, B)

	fmt.Println("A + B = ")
	for _, row := range result {
		fmt.Println(row)
	}
}
