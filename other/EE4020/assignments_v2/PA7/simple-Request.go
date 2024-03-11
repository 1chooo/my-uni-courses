package main
import "fmt"
import "bufio"
import "net"
import "net/http"


func check(e error) {
	if e != nil {
	panic(e)
	}
}
func main() {
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", "127.0.0.1:12007")
	defer ln.Close()
	conn, _ := ln.Accept()
	defer conn.Close()
	reader := bufio.NewReader(conn)
	req, err := http.ReadRequest(reader)
	check(err)
	fmt.Printf("Method: %s\n", req.Method)
	fmt.Printf("Host: %s\n", req.Host)
	fmt.Printf("User-Agent: %s\n", req.UserAgent())
	fmt.Print(req.URL)
}