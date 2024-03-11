/*
Created Date: 2023/12/04
HW: 30
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
)

func main() {
	// seasons := [4]string{"Q1", "Q2", "Q3", "Q4"}
	// location := [6]string{
	// 	"台北 - 桃園",
	// 	"台北 - 新竹",
	// 	"台北 - 台中",
	// 	"台北 - 嘉義",
	// 	"台北 - 高雄",
	// 	"台北 - 花蓮",
	// }
	prices := [6]int{44, 116, 241, 386, 544, 284}
	people := [4][6]int{
		{35273, 21534, 12573, 31567, 52386, 44138},
		{25673, 55728, 31245, 33278, 51342, 22464},
		{21345, 22179, 32189, 36296, 33106, 43278},
		{53278, 32785, 43167, 21367, 44579, 32685},
	}

	var revenue [4][6]int

	for i := 0; i < len(people); i++ {
		for j := 0; j < len(people[i]); j++ {
			revenue[i][j] = prices[j] * people[i][j]
		}
	}

	var seasonTotal [4]int

	for i := 0; i < len(revenue); i++ {
		total := 0
		for j := 0; j < len(revenue[i]); j++ {
			total += revenue[i][j]
		}
		seasonTotal[i] = total
	}

	fmt.Println(seasonTotal)
}
