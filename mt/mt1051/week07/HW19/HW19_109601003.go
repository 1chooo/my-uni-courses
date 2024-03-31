/*
Created Date: 2023/10/30
HW: 19
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func main() {
	LA := []int{18, 25, 33, 8, 12, 18, 46}
	fmt.Println("1. LA =", LA)

	LA = append(LA, 57)
	fmt.Println("2. LA =", LA)

	count := 0
	for _, value := range LA {
		if value == 18 {
			count++
		}
	}
	fmt.Println("3. LA 裡 18 有幾個:", count)

	fmt.Println("4. LA length =", len(LA))

	LA = append(LA, 32, 18, 92)
	fmt.Println("5. LA =", LA)

	index := -1
	for i, value := range LA {
		if value == 8 {
			index = i
			break
		}
	}
	fmt.Println("6. 8 在 LA 裡的 index:", index)

	LA = append(LA[:5], append([]int{55}, LA[5:]...)...)
	fmt.Println("7. LA =", LA)

	if len(LA) > 9 {
		LA = append(LA[:9], LA[10:]...)
	}
	fmt.Println("8. LA =", LA)

	index46 := -1
	for i, value := range LA {
		if value == 46 {
			index46 = i
			break
		}
	}
	if index46 != -1 {
		LA = append(LA[:index46], LA[index46+1:]...)
	}
	fmt.Println("9. LA =", LA)

	for i, j := 0, len(LA)-1; i < j; i, j = i+1, j-1 {
		LA[i], LA[j] = LA[j], LA[i]
	}
	fmt.Println("10. LA =", LA)

	for i := 0; i < len(LA); i++ {
		for j := i + 1; j < len(LA); j++ {
			if LA[i] > LA[j] {
				LA[i], LA[j] = LA[j], LA[i]
			}
		}
	}
	fmt.Println("11. LA =", LA)

	sum := 0
	for _, value := range LA {
		sum += value
	}
	fmt.Println("12. LA 中所有元素的總和:", sum)
}
