package main
import "fmt" 

//the capacity of a slice doubles any time it runs out of room
func main() {
	intSlice := []int{1, 2, 3} 
	for i := 4; i < 90; i++ {
		startCap := cap(intSlice)
		intSlice = append(intSlice, i)
		endCap := cap(intSlice)
		if (startCap != endCap) {
			fmt.Printf("on iteration %v the capacity changed from %v to %v\n", i, startCap, endCap)
		}
	}
}