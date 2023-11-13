package main 

import (
	"fmt"
	"math"
)

//types
type rover struct {
	gps
}

type gps struct {
	current, destination location
	world world
}
type location struct {
	lat, long float64
	name string
}
type world struct {
	radius float64
}

func (this location) description() string {
	return  fmt.Sprintf("%v, %v, %v", this.lat, this.long, this.name)
}

// distance calculation using the Spherical Law of Cosines.
func (w world) distance(p1, p2 location) float64 {
	s1, c1 := math.Sincos(rad(p1.lat))
	s2, c2 := math.Sincos(rad(p2.lat))
	clong := math.Cos(rad(p1.long - p2.long))
	return w.radius * math.Acos(s1*s2+c1*c2*clong)
}
// rad converts degrees to radians.
func rad(deg float64) float64 {
	return deg * math.Pi / 180
}

func (g gps) distance() float64 {
	return g.world.distance(g.current, g.destination)
}

func (g gps) message() string {
	return fmt.Sprintf("There are %v km untill the destination", g.distance())
}

func main() {
	bradbury := location{-4.5895, 137.4417, "Bradbury Landing"}
	elysium := location{4.5, 135.9, "Elysium Planitia"}

	var mars 	= world{radius: 3389.5}

	testGps := gps{world: mars, current: bradbury, destination: elysium}
	rovTest := rover{testGps}
	//**********This uses embedding to access gps.message***********
	fmt.Println(rovTest.message())
}