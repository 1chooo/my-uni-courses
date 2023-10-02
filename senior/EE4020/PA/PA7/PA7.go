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
	ln, _ := net.Listen("tcp", ":12003") 
	defer ln.Close()

	for {
		conn, _ := ln.Accept()
		//defer conn.Close()

		reader := bufio.NewReader(conn) 
		req, err := http.ReadRequest(reader) 
		check(err)

		request_file := req.URL.String()[1:]

		in_file, err := os.Open(request_file) 
		if err != nil {
			fmt.Printf("File not found.\n")
			conn.Close()
			continue
		}

	   	// get the file size
	   	stat, err := in_file.Stat()
	   	check(err)
	   	fmt.Printf("File size = %d\n", stat.Size())
	   	conn.Close()
	}
}