package main
import "fmt"



func drawLine() {
	fmt.Printf("=======================\n")
}
func printRow(val1 float64, val2 float64) {
	fmt.Printf("| %-9.4g| %-9.4g|\n", val1, val2)
}

type tempConv func(float64) float64

func celToFaren(temp float64) float64{
	return (temp * (9.0 / 5.0) + 32)
}

func farenToCel(temp float64) float64 {
	return (temp -32) * (5.0 / 9.0)
}


//takes in a function of type tempConv called conv
//also takes in the units that are being used and converted to
//prints a table of the origUnit being converted to convUnit
func drawTable(origUnit string, convUnit string, conv tempConv) {
	drawLine()
	fmt.Printf("| %-9s| %-9s|\n", origUnit, convUnit)
	drawLine()
	for temp := -40.0; temp <= 100; temp = temp + 5 {
		var convertedTemp float64 = conv(temp)
		printRow(temp, convertedTemp)
	}
	drawLine()
}

func main() {
	drawTable("C", "F", celToFaren)
	drawTable("F", "C", farenToCel)
}