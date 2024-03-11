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
	// Print the file size
	fi, err := file.Stat()
	// If an error occurs, print it and return
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(fi.Size())
}
