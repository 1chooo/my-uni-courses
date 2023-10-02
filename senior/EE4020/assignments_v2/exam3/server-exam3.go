package main
import "fmt"
import "bufio"
import "net"
import "time"
func check(e error) {
 if e != nil {
 panic(e)
 }
}
func handleConnection (c net.Conn, i int) {
 reader := bufio.NewReader(c)
 message, errr := reader.ReadString('\n')
 check(errr)
 fmt.Printf("%s", message)
 j := 0
 for (j < 10) {
 time.Sleep(1 * time.Second)
 fmt.Printf("client #%d processing: %d%% \n", i, 10*j)
 j++
 }
 time.Sleep(10 * time.Second)
 writer := bufio.NewWriter(c)
 newline := fmt.Sprintf("%d bytes received\n", len(message))
 _, errw := writer.WriteString(newline)
 check(errw)
 writer.Flush()
 c.Close()
}