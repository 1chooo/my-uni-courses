package main
import "fmt"
import "bufio"
import "net"
import "os"
func check(e error) {
	if e != nil {
		panic(e)
	}
}
func main() {
	conn, errc := net.Dial("tcp", "127.0.0.1:12007")
	check(errc)
	defer conn.Close()

	// Specify the input file
	fmt.Printf("Upload file name:")
	uploadName := ""
	fmt.Scanf("%s\n", &uploadName)
    file, err := os.Open(uploadName)
	check(err)
	defer file.Close()

	// Get the size of the file
	// finfo, err := file.Stat()
	finfo,err:=os.Stat(uploadName)
	check(err)
	size := finfo.Size()

	// Declare the file reader and server writer.
	myfileScanner := bufio.NewScanner(file)
	writer := bufio.NewWriter(conn)

	// send the file size to the server.
	newline := fmt.Sprintf("%d\n", size)
	writer.WriteString(newline)

	// Send the entire file content.
	for myfileScanner.Scan() {
		text := fmt.Sprintf("%s\n", myfileScanner.Text())
		writer.WriteString(text)
		writer.Flush()
	}

	// Receive message back from the server.
	ServerScanner := bufio.NewScanner(conn)
	if ServerScanner.Scan() {
		fmt.Printf("Server replies: %s\n", ServerScanner.Text())
	}
}