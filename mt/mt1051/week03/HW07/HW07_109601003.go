// Date: 2023/09/25
// HW: 07
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
	"math"
)

func main() {
	// 输入一个数值 E
	var E float64
	fmt.Print("请输入一个数值 E: ")
	fmt.Scan(&E)

	// 根据条件进行操作
	var result float64
	if E < 50 {
		result = math.Sqrt(E) * 10
	} else {
		result = E + 12
	}

	// 输出最终结果
	fmt.Println("最终结果为:", result)
}
