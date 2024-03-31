/*
Created Date: 2023/11/27
HW: exam
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func partition(nums []int, low, high int) int {
	pivot := nums[high]
	i := low - 1

	for j := low; j < high; j++ {
		if nums[j] >= pivot {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	nums[i+1], nums[high] = nums[high], nums[i+1]
	return i + 1
}

func quickselect(nums []int, low, high, k int) int {
	if low <= high {
		pivotIndex := partition(nums, low, high)

		if pivotIndex == k {
			return nums[pivotIndex]
		} else if pivotIndex < k {
			return quickselect(nums, pivotIndex+1, high, k)
		} else {
			return quickselect(nums, low, pivotIndex-1, k)
		}
	}
	return -1 // Error case
}

func findKthLargest(nums []int, k int) int {
	return quickselect(nums, 0, len(nums)-1, k-1)
}

func main() {
	numbers := []int{39, 82, 12, 54, 34, 23, 52, 19, 53, 55, 73, 71, 62, 11}
	k := 5 // Find the 5th largest number

	result := findKthLargest(numbers, k)
	fmt.Printf("The %dth largest number is: %d\n", k, result)
}
