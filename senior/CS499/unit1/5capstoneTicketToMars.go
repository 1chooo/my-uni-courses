package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	
	const tripCount = 10
	const marsDist = 62100000 //km

	fmt.Printf("%-15v %6v %-11v %5v\n", "Spaceline", "Days", "Trip type", "Price")
	fmt.Println("=========================================")
	for i := 0; i < tripCount; i++ {
		
		//pick randomly between the 2 lines
		var line = ""
		if rand.Intn(2) == 1 {
			line = "Virgin Galactic"
		} else {
			line = "SpaceX"
		}

		//generate a random speed between 16 and 30 km/s
		var speed = rand.Intn(15) + 16	//km/s
		//calculate duration from the speed
		var duration = (marsDist / (speed)) / 86400

		//calculate one way price based on speed
		var price = 36 + speed - 16 		//million dollars

		//randomly choose a trip type
		var tripType = ""
		if rand.Intn(2) == 1 {
			tripType = "Round-trip"
			price = price * 2
			duration = duration * 2
		} else {
			tripType = "One-way"
		}
		fmt.Printf("%-15v %6v %-11v %v %3v\n", line, duration, tripType, "$", price)
	}
}