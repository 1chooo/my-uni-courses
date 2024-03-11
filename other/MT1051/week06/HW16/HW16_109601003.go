/*
Created Date: 2023/10/23
HW: 16
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"math"
)

func supplyPrice(P float64) float64 {
	return 43.3 + 1.25*P
}

func demandPrice(P float64) float64 {
	return 96.3 - 2.13*P
}

func main() {
	i := 0.0
	tolerance := 0.0001

	for {
		Qs := supplyPrice(i)
		Qs = round(Qs, 3)
		Qd := demandPrice(i)
		Qd = round(Qd, 3)

		if delta := Qs - Qd; delta < tolerance && delta > -tolerance {
			fmt.Printf("均衡价格 (P) = %.3f\n", i)
			fmt.Printf("均衡数量 (Q) = %.3f\n", Qs)
			break
		}

		i += 0.0001
	}
}

func round(x float64, decimals int) float64 {
	pow := math.Pow(10, float64(decimals))
	return math.Round(x*pow) / pow
}
