// Extend exam2-p13-2.go to exam2-p20-3.go such that it connects to the server running on port 12000, sends “play\n”, receives a line of message from the server, prints the message on the screen, and then closes the connection.
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// Connect to the server running on port 12000
	conn, err := net.Dial("tcp", ":12000")
	if err != nil {
		fmt.Println("Error connecting:", err)
		os.Exit(1)
	}

	// Send the string "play\n" to the server
	writer := bufio.NewWriter(conn)
	writer.WriteString("play\n")
	writer.Flush()

	// Read a line of message from the server
	reader := bufio.NewReader(conn)
	message, err := reader.ReadString('\n')
	fmt.Println(message)

	// Close the connection
	conn.Close()
}
