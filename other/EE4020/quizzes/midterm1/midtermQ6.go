package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("tcp", "127.0.0.1:11992")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()
	// Send "hello!\n"
	writer := bufio.NewWriter(conn)
	writer.WriteString("hello!\n")
	writer.Flush()
}
