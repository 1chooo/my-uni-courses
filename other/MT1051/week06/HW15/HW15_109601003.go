/*
Created Date: 2023/10/23
HW: 15
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

type CoinProblem struct {
	num10, num5, num1 int
}

func (cp *CoinProblem) calculateCoins() {
	for cp.num10 = 0; cp.num10 <= 20; cp.num10++ {
		for cp.num5 = 0; cp.num5 <= 40; cp.num5++ {
			cp.num1 = 20 - cp.num10 - cp.num5

			if cp.num1 >= 0 && cp.num5 >= 0 && cp.num10 >= 0 && (cp.num10*10+cp.num5*5+cp.num1 == 108) {
				return
			}
		}
	}
}

func (cp *CoinProblem) printResult() {
	fmt.Printf("10 元硬幣數量：%d\n", cp.num10)
	fmt.Printf("5  元硬幣數量：%d\n", cp.num5)
	fmt.Printf("1  元硬幣數量：%d\n", cp.num1)
}

func main() {
	coinProblem := CoinProblem{}
	coinProblem.calculateCoins()
	coinProblem.printResult()
}
