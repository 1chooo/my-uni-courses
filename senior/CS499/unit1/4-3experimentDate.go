package main

import (
    "fmt"
    "math/rand"
)

func main() {
	for i:= 0; i < 100; i++ {
		year := rand.Intn(5000) - 2000
		month := rand.Intn(12) + 1
		daysInMonth := 31
		var era = "invalid year"
		if year < 0 {
			era = "BC"
			year = year * -1
		} else {
			era = "AD"
		}

		switch month {
		case 2:
			if year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0) {
				daysInMonth = 29
			} else {
				daysInMonth = 28
			}
		case 4, 6, 9, 11:
			daysInMonth = 30
		}

		day := rand.Intn(daysInMonth) + 1
		fmt.Println(era, year, month, day)
	}
}