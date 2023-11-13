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

// location with a latitude, longitude in decimal degrees.
type location struct {
	Lat Coordinate 	`json:"latitude"`
	Long Coordinate	`json:"longitude`
}



func (c Coordinate) decimal() float64 {
	sign := 1.0
	switch c.h {
	case 'S', 'W', 's', 'w':
		sign = -1
	}
	return sign * (c.d + c.m/60 + c.s/3600)
}

// String formats a DMS coordinate.
func (c Coordinate) String() string  {
	return fmt.Sprintf("%v°%v'%.1f\" %c", c.d, c.m, c.s, c.h)
}

func (c Coordinate) MarshalJSON() ([]byte, error) {
	return json.Marshal(struct {
		DD  float64 `json:"decimal"`
		DMS string  `json:"dms"`
		D   float64 `json:"degrees"`
		M   float64 `json:"minutes"`
		S   float64 `json:"seconds"`
		H   string  `json:"hemisphere"`
  }{
		DD:  c.decimal(),
		DMS: c.String(),
		D:   c.d,
		M:   c.m,
		S:   c.s,
		H:   string(c.h),
  })
}
// String formats a location with latitude, longitude.
func (l location) String() string {
	return fmt.Sprintf("%v, %v", l.Lat, l.Long)
}

func main() {
	elysium := location{
		 Lat:  Coordinate{4, 30, 0.0, 'N'},
		 Long: Coordinate{135, 54, 0.0, 'E'},
	}

	bytes, err := json.MarshalIndent(elysium, "", "  ")
	if err != nil {
		 fmt.Println(err)
		 os.Exit(1)
	}

	fmt.Println(string(bytes))
}