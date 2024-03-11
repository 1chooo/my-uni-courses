package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Prompt the user for a filename
	fmt.Print("Enter your filename: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	// Read the file and ensure it exists
	filename := scanner.Text()
	file, err := os.Open(filename)

	// If an error occurs, print it and return
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	// Read each character from the file, if it is not '\r', print it out std.out
	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		for _, char := range line {
			if char != '\r' {
				fmt.Printf("%c", char)
			}
		}
		fmt.Println()
	}
}
