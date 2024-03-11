package main
import "fmt"
import "bufio"
import "net"
import "strconv"
import "strings"
import "os"
func check(e error) {
 if e != nil {
 panic(e)
 }
}
func main() {
 fmt.Println("Launching server...")
 ln, _ := net.Listen("tcp", ":12007")
 conn, _ := ln.Accept()
 defer ln.Close()
 defer conn.Close()

 outputName := "whatever.txt"
 fO, err := os.Create(outputName)
 check(err)
 defer fO.Close()

 count := 0
 reader := bufio.NewReader(conn)
 line, _ := reader.ReadString('\n')
 line = strings.Split(line,"\n")[0]
 filesize, _ := strconv.Atoi(line)

 writer := bufio.NewWriter(fO)
 writerServer := bufio.NewWriter(conn)

 lineCount := 1
 for {
	line, _ := reader.ReadString('\n')
	tmpcount := len([]rune(line))
	count = count + tmpcount + 1
	addtext := strconv.Itoa(lineCount) + " " + line
	writer.WriteString(addtext)
	fmt.Printf(addtext)
	lineCount = lineCount + 1
	writer.Flush()
	if (count >= filesize){
		break;
	}
 }
 
 finfo,err:=os.Stat(outputName)
 check(err)
 newsize := finfo.Size()


 newline := fmt.Sprintf("%d bytes received. (Orginal file size)\n%d bytes sent. (New file size)\n", filesize, newsize)
 fmt.Print(newline)
 writerServer.WriteString(newline)


}