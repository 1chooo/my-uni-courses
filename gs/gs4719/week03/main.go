package main

import (
	"fmt"
	"math"
)

func main() {
    // Checking if 'if' is a keyword
    isIfKeyword := isKeyword("if")
    fmt.Printf("Is 'if' a keyword? %t\n", isIfKeyword)

    // Checking if 'IF' is a keyword
    isIFKeyword := isKeyword("IF")
    fmt.Printf("Is 'IF' a keyword? %t\n", isIFKeyword)

    // Integer addition
    result1 := 23 + 45
    fmt.Println(result1)

    // Integer subtraction
    result2 := 59 - 22
    fmt.Println(result2)

    // Integer multiplication
    result3 := 43 * 3
    fmt.Println(result3)

    // Integer square
    result4 := 8 * 8 // Integer square
    fmt.Println(result4)

    // Integer division (floating-point result)
    result5 := float64(16) / 4
    fmt.Println(result5)

    // Integer division (integer result)
    result6 := 16 / 4
    fmt.Println(result6)

    // Integer division (floating-point result)
    result7 := float64(16) / 4.0
    fmt.Println(result7)

    // Modulus
    result8 := 15 % 4
    fmt.Println(result8)

    // Modulus (floating-point result)
    result9 := float64(15) / 4.0
    fmt.Println(result9)

    // Defining and initializing a variable x
    x := 5
    fmt.Println(x)

    // Increasing the value of x
    x = x + 1
    fmt.Println(x)

    // Increasing the value of x (simplified syntax)
    x++
    fmt.Println(x)

    // Decreasing the value of x
    x--
    fmt.Println(x)

    // Negating x
    x = -x
    fmt.Println(x)

    // Defining and initializing a variable y
    y := 3
    fmt.Println(x, y)

    // Raising y to the power of x
    y = int(math.Pow(float64(x), float64(y)))
    fmt.Println(x, y)

    // Large number calculation
    bigNumber1 := math.Pow(33, 999)
    fmt.Println(bigNumber1)

    // Large number calculation (floating-point result)
    bigNumber2 := math.Pow(33.0, 999)
    fmt.Println(bigNumber2)

    // Integers
    fmt.Println(36)

    // Binary number 0b1011, equivalent to decimal 11
    fmt.Println(11)

    // Octal number 0o36, equivalent to decimal 30
    fmt.Println(30)

    // Hexadecimal number 0x36, equivalent to decimal 54
    fmt.Println(54)

    // Addition with different number representations
    result10 := 11 + 3 + 9 + 17
    fmt.Println(result10)

    // Floating-point number 31.2
    fmt.Println(31.2)

    // Converting a floating-point number to an integer (result is 31)
	intResult := int(math.Round(31.2))
    fmt.Println(intResult)

    // Integer 20
    fmt.Println(20)

    // Converting an integer to a floating-point number (result is 20.0)
    floatResult := float64(20)
    fmt.Println(floatResult)

    // Rounding a floating-point number to two decimal places (result is 25.35)
    roundedResult := round(25.346, 2)
    fmt.Println(roundedResult)

    // Defining an integer variable x with a value of 33
    x = 33
    fmt.Printf("type(x) = %T\n", x)
    fmt.Printf("x = %v\n", x)

    // Identifiers in Go
    fmt.Println(isIdentifier("abc"))  // true
    fmt.Println(isIdentifier("99a"))  // false
    fmt.Println(isIdentifier("_"))    // true
    fmt.Println(isIdentifier("for"))  // true
}

// isKeyword checks if a string is a keyword in Go
func isKeyword(str string) bool {
	// List of Go keywords
	keywords := map[string]bool{
		"break":       true,
		"default":     true,
		"func":        true,
		"interface":   true,
		"select":      true,
		"case":        true,
		"defer":       true,
		"go":          true,
		"map":         true,
		"struct":      true,
		"chan":        true,
		"else":        true,
		"goto":        true,
		"package":     true,
		"switch":      true,
		"const":       true,
		"fallthrough": true,
		"if":          true,
		"range":       true,
		"type":        true,
		"continue":    true,
		"for":         true,
		"import":      true,
		"return":      true,
		"var":         true,
	}

	return keywords[str]
}

// isIdentifier checks if a string is a valid identifier in Go
func isIdentifier(str string) bool {
	if len(str) == 0 {
		return false
	}

	for _, char := range str {
		if !isLetter(char) && !isDigit(char) && char != '_' {
			return false
		}
	}

	// 這裡添加了對第一個字符是否為字母的檢查
	if !isLetter(rune(str[0])) {
		return false
	}

	return true
}


// isLetter checks if a character is a letter (uppercase or lowercase)
func isLetter(char rune) bool {
	return ('a' <= char && char <= 'z') || ('A' <= char && char <= 'Z')
}

// isDigit checks if a character is a digit
func isDigit(char rune) bool {
	return '0' <= char && char <= '9'
}

// round rounds a floating-point number to a specified number of decimal places
func round(num float64, decimalPlaces int) float64 {
	shift := math.Pow(10, float64(decimalPlaces))
	return math.Round(num*shift) / shift
}
