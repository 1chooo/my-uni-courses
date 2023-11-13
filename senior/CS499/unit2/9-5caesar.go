package main
import "fmt"

func main() {
	var quote string = "L fdph, L vdz, L frqtxhuhg"
	//for index i and character c in the string quote
	for _, char := range quote {
		if char >= 'A' && char <= 'Z' {
			char = char - 3
			if char < 'A' {
				char = char + 26
			}
		}
		if char >= 'a' && char <= 'z' {
			char = char - 3
			if (char < 'a') {
				char = char + 26
			}
		}
		fmt.Printf("%c", char)
	}
}