/*
Created Date: 2023/11/23
HW: 24
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func findMin(nums []int) {
	min := nums[0]
	for _, num := range nums {
		if num < min {
			min = num
		}
	}
	fmt.Printf("The minimum value is %d\n", min)
}

func main() {
	listA := []int{23, 78, 45, 8, 32, 56, 14, 25, 4, 62}
	findMin(listA)
}
