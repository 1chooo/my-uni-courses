package main
import "fmt"
import "bufio"
import "net"
func check(e error) {
 if e != nil {
 panic(e)
 }
}
func main() {
 conn, errc := net.Dial("tcp", "127.0.0.1:12007")
 check(errc)
 defer conn.Close()
 writer := bufio.NewWriter(conn)
 len, errw := writer.WriteString("Hello World!\n happy new year \n")
 check(errw)
 fmt.Printf("Send a string of %d bytes\n", len)
 writer.Flush()
 reader := bufio.NewReader(conn)
 message, errr := reader.ReadString('\n')
 check(errr)
 fmt.Printf("Server replies: %s", message)
}