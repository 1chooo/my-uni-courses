package main

import "fmt"

func main() {
	for i, j := 2, 1; j < 10; {
		tmp := i * j
		fmt.Printf("%dx%d", i, j)
		if tmp >= 10 {
			fmt.Printf("=")
		} else {
			fmt.Printf("= ")
		}
		if i == 9 {
			fmt.Printf("%d\n", i*j)
		} else {
			fmt.Printf("%d ", i*j)
		}

		if i == 9 {
			i = 2
			j++
		} else {
			i++
		}
	}
}
