package main

import (
  "fmt"
  "bufio"
  "net/http"
  "crypto/tls"
)

func check(e error) {
  if e != nil {
	panic(e)
  }
}

func main() {
  // tls.LoadX509KeyPair takes two parameters, public and private keys
  cert, _ := tls.LoadX509KeyPair("server.cer", "server.key")
  // Configures the TLS socket, Certificaes is defined as an array of certificate chains
  config := tls.Config{Certificates: []tls.Certificate{cert}}

  fmt.Println("Launching server...")
  // New API defined in the crypto/tls package is equivalent to net.Listen()
  ln, _ := tls.Listen("tcp", ":12001", &config)
  defer ln.Close()
  conn, _ := ln.Accept()
  defer conn.Close()

  reader := bufio.NewReader(conn)
  req, _ := http.ReadRequest(reader)
  fmt.Printf("Method: %s\n", req.Method)

  fmt.Fprintf(conn, "HTTP/1.1 404 Not Found\r\n")
  fmt.Fprintf(conn, "Date: ...\r\n")
  fmt.Fprintf(conn, "\r\n")
  fmt.Fprintf(conn, "File not found\r\n")
  fmt.Fprintf(conn, "\r\n")
}
