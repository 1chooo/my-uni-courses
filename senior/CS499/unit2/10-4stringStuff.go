package main

import (
	"fmt"
	"strconv"
)

func main() {
	var countdown int = 10

	var str string = "Launch in T minus " + strconv.Itoa(countdown) + " seconds."
	fmt.Println(str)
}