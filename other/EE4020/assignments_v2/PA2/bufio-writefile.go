package main
import "fmt"
import "os"
import "bufio"
func check(e error) {
 if e != nil {
 panic(e)
 }
}
func main() {
f, err := os.Create("PA2-output.txt")
check(err)
defer f.Close()
writer := bufio.NewWriter(f)
len, _ := writer.WriteString("This is a test!")
fmt.Println(len)
writer.Flush()
}