package main
import (
	"fmt"
	"math"
)

type world struct {
	radius float64
}

// Coordinate in degrees, minutes, seconds in a N/S/E/W hemisphere.
type Coordinate struct {
	d, m, s float64
	h       rune
}

type Location struct {
	Lat, Long float64
}

// distance calculation using the Spherical Law of Cosines.
func (w world) distance(p1, p2 Location) float64 {
	s1, c1 := math.Sincos(rad(p1.Lat))
	s2, c2 := math.Sincos(rad(p2.Lat))
	clong := math.Cos(rad(p1.Long - p2.Long))
	return w.radius * math.Acos(s1*s2+c1*c2*clong)
}

// rad converts degrees to radians.
func rad(deg float64) float64 {
	return deg * math.Pi / 180
}

// decimal converts a d/m/s Coordinate to decimal degrees.
func (c Coordinate) decimal() float64 {
	sign := 1.0
	switch c.h {
	case 'S', 'W', 's', 'w':
		sign = -1
	}
	return sign * (c.d + c.m/60 + c.s/3600)
}

func newLocation(lat, long Coordinate) Location {
	return Location{lat.decimal(), long.decimal()}
}

func main() {
	// var mercury = world{radius: 2439.7}
	// var venus 	= world{radius: 6051.8}
	// var earth 	= world{radius: 6371.0}
	var mars 	= world{radius: 3389.5}
	// var jupiter = world{radius: 69911}
	// var saturn 	= world{radius: 58232}
	// var uranus 	= world{radius: 25362}
	// var neptune = world{radius: 24622}

	lat := Coordinate{14, 34, 6.2, 'S'}
	long := Coordinate{175, 28, 21.5, 'E'}
	columbia := newLocation(lat, long)

	lat2 := Coordinate{1, 56, 46.3, 'S'}
	long2 := Coordinate{354, 28, 24.2, 'E'}
	opportunity := newLocation(lat2, long2)
	dist := mars.distance(columbia, opportunity)
	fmt.Println(dist)
}