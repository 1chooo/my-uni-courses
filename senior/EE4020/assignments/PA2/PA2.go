package main

import (
	"bufio"
	"fmt"
	"os"
)

// If we run into an error while assessing the file, panic
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Prompt the user for the input and output file names
	inputFileName := ""
	outputFileName := ""
	// NOTE: Assumption made user will enter in valid format
	fmt.Println("Enter the input file name:")
	fmt.Scanf("%s", &inputFileName)
	fmt.Println("Enter the output file name:")
	fmt.Scanf("%s", &outputFileName)

	// Open the input/output files for reading and writing
	inputFile, err := os.Open(inputFileName)
	check(err)
	outputFile, err := os.Create(outputFileName)
	check(err)

	// Iterate through the input file line and prepend current line count
	scanner := bufio.NewScanner(inputFile)
	lineCount := 0
	// While scanner.Scan() returns true, we have not reached the end of the file
	for scanner.Scan() {
		lineCount++
		// Write each line to the output file
		fmt.Fprintf(outputFile, "%d %s\n", lineCount, scanner.Text())
	}
}
