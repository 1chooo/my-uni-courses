package main

import "fmt"

type celsius float64
func (temp celsius) fahrenheit() fahrenheit {
	return fahrenheit(temp * (9.0 / 5.0) + 32)
}
func (temp celsius) kelvin() kelvin {
	return kelvin(temp + 273.15)
}


type fahrenheit float64
func (temp fahrenheit) celsius() celsius {
	return celsius((temp - 32) * (5.0 / 9.0))
}
func (temp fahrenheit) kelvin() kelvin {
	return kelvin(((temp - 32) * (5.0 / 9.0)) + 273.15)
}


type kelvin float64
func (temp kelvin) celsius() celsius {
	return celsius(temp - 273.15)
}
func (temp kelvin) fahrenheit() fahrenheit {
	return fahrenheit(((temp - 273.15) * (9.0 / 5.0)) + 32.0)
}



func main() {
	var k kelvin = 12
    fmt.Printf("%v deg kelvin to farenheight = %v\n", k, k.fahrenheit())
}
