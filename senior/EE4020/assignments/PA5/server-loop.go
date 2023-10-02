package main

import (
  "fmt"
  "bufio"
  "net"
)

func check(e error) {
  if e != nil {
	panic(e)
  }
}

func main() {
  fmt.Println("Launching server...")
  ln, _ := net.Listen("tcp", ":12001")
  defer ln.Close()

  for {
	conn, _ := ln.Accept()
	defer conn.Close()

	reader := bufio.NewReader(conn)
	message, err := reader.ReadString('\n')
	check(err)
	fmt.Printf("%s", message)

	writer := bufio.NewWriter(conn)
	newline := fmt.Sprintf("%d bytes received\n", len(message))
	_, errw := writer.WriteString(newline)
	check(errw)
	writer.Flush()
  }
}

