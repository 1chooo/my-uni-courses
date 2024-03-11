// Develop exam2-p14-1.go running on your exam port # such that it allows multiple clients such as your exam2-p13-1.go to connect and then close.
package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", ":30102")
	defer ln.Close()

}
