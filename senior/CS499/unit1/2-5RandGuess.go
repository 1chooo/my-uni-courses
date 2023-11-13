package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var num = rand.Intn(34) + 1
	fmt.Println("number between 1 and 34 =", num)
	num = rand.Intn(10) + 1
	fmt.Println("number between 1 and 10 =", num)
}