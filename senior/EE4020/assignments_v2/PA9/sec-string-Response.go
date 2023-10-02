package main
import "fmt"
import "bufio"
import "net/http"
import "crypto/tls"
func check(e error) {
 if e != nil {
 panic(e)
 }
}

func main() {
	cert, _ := tls.LoadX509KeyPair("server.cer", "server.key")
	config := tls.Config{Certificates: []tls.Certificate{cert}}
	fmt.Println("Launching server...")
	ln, _ := tls.Listen("tcp", ":12007", &config)
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