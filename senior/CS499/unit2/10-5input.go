package main

import "fmt"

func main() {
	var str string = "n"
	var output bool
	if str == "true" || str == "yes" || str == "1" {
		output = true
	} else if str == "false" || str == "no" || str == "0" {
		output = false
	} else {
		fmt.Println("error")
	}
	fmt.Println(output)
}