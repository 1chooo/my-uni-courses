// Develop exam2-p14-2.go such that it allows multiple clients such as your exam2-p13-2.go to connect, send “play\n”, and then close.
package main

import (
	"net"
)

func main() {
	ln, _ := net.Listen("tcp", ":30102")
	defer ln.Close()

	for {
		// Wait for a connection.
		conn, _ := ln.Accept()
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
}
