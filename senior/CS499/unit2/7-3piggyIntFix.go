package main

import (
	"fmt"
	"math/rand"
	"time"

)

func main() {
	var balance = 0.0
	for balance / 100 <= 7 {
		rand.Seed(time.Now().UnixNano())
		var chooseNum = rand.Intn(2)
		if (chooseNum == 0) {
			balance = balance + 5
		} else if (chooseNum == 1) {
			balance = balance + 10
		} else {
			balance = balance + 25
		}
		fmt.Printf("Balance = %v\n", balance / 100)
	}

}