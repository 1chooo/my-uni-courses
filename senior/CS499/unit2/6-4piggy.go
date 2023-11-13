package main

import (
	"fmt"
	"math/rand"
	"time"

)

func main() {
	var balance float64 = 0
	for balance <= 7 {
		rand.Seed(time.Now().UnixNano())
		var chooseNum = rand.Intn(2)
		if (chooseNum == 0) {
			balance = balance + .05
		} else if (chooseNum == 1) {
			balance = balance + .10
		} else {
			balance = balance + .25
		}
		fmt.Printf("Balance = %f\n", balance)
	}

}