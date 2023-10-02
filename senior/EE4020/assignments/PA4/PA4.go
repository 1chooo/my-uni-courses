// Listen at 12001 until there's an upload request
// Read from the socket first the file size (given in a single line)
// Read from the socket one line at a time
// Prepend the line count to each line and store new line into a new file called: whatever.txt
// Repeat (3) and (4) until all lines in the file are processed
// Send a message to client the original and new file sizes
// Close the connection and terminate the program

package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

// Function to check for errors, if not null, panic
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Launch the server on local IP at port 12001
	fmt.Println("Launching server... at port 12001")
	ln, _ := net.Listen("tcp", ":12001")
	conn, _ := ln.Accept()
	defer ln.Close()
	defer conn.Close()

	// Read from the socket first the file size, demarcated by a newline
	reader := bufio.NewReader(conn)
	initialFileSize, err := reader.ReadString('\n')
	check(err)

	// Create a new file to write to
	file, err := os.Create("whatever.txt")
	check(err)
	defer file.Close()

	// While there are still lines to read, read one line at a
	// time and prepend the line count to each line
	lineCount := 0
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		lineCount++
		newLine := fmt.Sprintf("%d %s", lineCount, line)
		file.WriteString(newLine)
	}

	// Check the size of the new file
	fileInfo, err := file.Stat()
	check(err)
	newFileSize := fileInfo.Size()

	// Send a message to client the original and new file sizes
	writer := bufio.NewWriter(conn)
	writer.WriteString(fmt.Sprintf("Initial file size: %s", initialFileSize))
	writer.WriteString(fmt.Sprintf("New file size: %d", newFileSize))

}
