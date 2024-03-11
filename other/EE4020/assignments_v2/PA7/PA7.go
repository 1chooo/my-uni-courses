package main
import "fmt"
import "bufio"
import "net"
import "net/http"
import "os"


func check(e error) {
	if e != nil {
	panic(e)
	}
}
func main() {
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", "127.0.0.1:12007")
	defer ln.Close()
	for{
		// looping listening...
		conn, _ := ln.Accept()
		reader := bufio.NewReader(conn)

		// Read the HTTP request
		req, err := http.ReadRequest(reader) 
		check(err)

		// Interpret the URL of request.
		requestFileName := "." + req.URL.String()

		// check if the requested file is in this folder.
		file, err := os.Open(requestFileName)
		if (err != nil || req.URL.String()=="/"){
			fmt.Println("File not found.")
		}else{
			finfo,err:=os.Stat(requestFileName)
			check(err)
			size := finfo.Size()
			fmt.Printf("File size: %d\n", size)
		}
		file.Close()
		conn.Close()
	}
	
}