package main
import (
	"fmt"
	"encoding/json"
	"os"
)


// Coordinate in degrees, minutes, seconds in a N/S/E/W hemisphere.
type Coordinate struct {
	d, m, s float64
	h       rune
}

type Location struct {
	Lat, Long float64
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
	// Bradbury Landing: 4°35'22.2" S, 137°26'30.1" E
	lat := Coordinate{4, 35, 22.2, 'S'}
	long := Coordinate{137, 26, 30.12, 'E'}
	fmt.Println(lat.decimal(), long.decimal())

	test := newLocation(lat, long)
	bytes, err := json.Marshal(test)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
  	}
	fmt.Println(string(bytes))
}