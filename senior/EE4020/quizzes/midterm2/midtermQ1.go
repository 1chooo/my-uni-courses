// Develop exam2-p13-1.go such that it connects to the server running on port 12000 and then closes the connection.

package main

import (
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
	// Close the connection
	conn.Close()
}
