package main

import "fmt"

func main() {
	for count := 10; count > 0; count-- {
		fmt.Println("count is initialized with short var declaration, COUNT=", count)
	}
}