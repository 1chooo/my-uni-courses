package main 

import "fmt"

type planets []string
func (origPlanets planets) terraform() {
	prefix := "New"
	for i := range origPlanets {
		origPlanets[i] = prefix + origPlanets[i]
	}
}

func main() {
	var p planets = []string{"Venus", "Earth"}
	p.terraform()
	fmt.Println(p)
}