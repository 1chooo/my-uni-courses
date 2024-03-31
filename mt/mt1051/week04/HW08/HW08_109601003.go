// Date: 2023/10/02
// HW: 08
// Author: 林群賀
// Student Number: 109601003

package main

import "fmt"

func main() {
	sum := 0

	for i := 1; i < 100; i += 2 {
		sum += i
	}

	fmt.Println(sum)
}
