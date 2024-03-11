/*
Created Date: 2023/12/11
HW: 34
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"time"
)

func main() {
	presentTime := time.Now()
	fmt.Println("Time:", presentTime)

	timeAlert := time.Date(2023, 12, 11, 9, 22, 0, 0, time.UTC)
	if presentTime.After(timeAlert) {
		fmt.Println("Time is up!")
	}

	deltaTime := time.Date(0, 0, 0, 2*7+3, 5, 15, 25*1000000, time.UTC)
	fmt.Println("DeltaTime:", deltaTime)

	timeNew := presentTime.Add(deltaTime)
	fmt.Println("Time after DeltaTime is:", timeNew)
	fmt.Println("Time after DeltaTime is:", timeNew)
}
