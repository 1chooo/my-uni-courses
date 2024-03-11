// Objectives
// Sends first the file size (# in size line)
// Send the file contents
// Receive a message back from server
// Print the server response
// Close the connection and terminate the program

package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Verify that this is the command to connect to pollys server
	conn, errc := net.Dial("tcp", "127.0.0.1:12000")
	check(errc)
	defer conn.Close()

	// Prompt the user for upload file name
	uploadFileName := ""
	fmt.Print("Please enter the upload file name: ")
	fmt.Scanf("%s", &uploadFileName)

	// Open the file
	file, errc := os.Open(uploadFileName)
	check(errc)
	defer file.Close()

	// Calculate its file size
	stat, _ := file.Stat()
	sizeBytes := stat.Size()
	fmt.Printf("Send the file size first: %d\n", sizeBytes)

	// Create a buffered writer to send the file size
	writer := bufio.NewWriter(conn)
	_, errw := writer.WriteString(fmt.Sprintf("%d", sizeBytes))
	check(errw)
	writer.Flush()

	// Read the file contents line by line and keep it as a string
	fileContents := ""
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fileContents += scanner.Text()
	}

	// Send the file contents
	_, errw = writer.WriteString(fileContents)
	check(errw)
	writer.Flush()

	// // Receive a message back from server
	response := bufio.NewScanner(conn)
	if response.Scan() {
		fmt.Printf("Server replies: %s\n", response.Text())
	}
}
