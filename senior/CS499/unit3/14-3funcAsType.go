package main
import "fmt"

func main() {
	//function signatures can be declared as types
	type getRowFn func(rows int) (string, string)
	//those types can then be used in function declarations as parameter types
	func drawTable(rows int, fn getRowFn)
}