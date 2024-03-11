package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("tcp", "127.0.0.1:11993")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()
	// Send "hello!\n"
	writer := bufio.NewWriter(conn)
	writer.WriteString("hello!\n")
	writer.Flush()

	// Read the response
	scanner := bufio.NewScanner(conn)
	if scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
