package main

import (
	"fmt"
	"strings"
)

func main() {
	var plainText string = "your message here"
	var keyword string = "GOLANG"
	var cipheredText string = ""

	//format the text to the preconditions from the assignment description
	plainText = strings.ToUpper(plainText)
	plainText = strings.ReplaceAll(plainText, " ", "")
	fmt.Println(plainText)


	for i, char:= range plainText {
		//converts char to a ascii value
		var asciiChar byte = byte(char)
		//determine the keywords letter for this index of the message
		var keyLetter byte = keyword[i % len(keyword)]
		var offSet = keyLetter - 'A'
		//fmt.Printf("Offset = %v\n", offSet)
		//subtract its ascii code from character c's ascii code
		var cipheredLetter byte = asciiChar - offSet
		//if the character would be less then A wrap it around the alphabet
		if cipheredLetter < 'A' {
			cipheredLetter = cipheredLetter + 26
		}
		//concatenate it to the ciphered string we are building
		cipheredText = cipheredText + string(cipheredLetter)
	}

	fmt.Println(cipheredText)
}