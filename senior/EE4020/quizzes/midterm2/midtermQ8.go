// Develop exam2-p14-3.go such that it allows multiple clients such as your exam2-p13-3.go to connect, send “play\n”, receive a line of response from your exam2-p14-3.go saying “Welcome to The Price is Right! Let’s guess the price of a 12-person tent.\n” and then close.
package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	fmt.Println("Launching server... ")
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
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		if scanner.Text() == "play" {
			fmt.Fprintf(conn, "Welcome to The Price is Right! Let’s guess the price of a 12-person tent.\n")
		}
	}
}
