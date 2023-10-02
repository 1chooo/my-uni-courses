package main

import "fmt"
import "bufio"
import "net"
import "net/http"
import "os"
//import "net/url"

// turn it into method
func check(e error) bool {
	if e != nil {
		panic(e)
	}
	return (e != nil)
}

func checkFile(e error) bool {
	if e != nil {
		return e != nil
	}
	return false
}

func handleConnection(conn net.Conn){
		
		
		reader := bufio.NewReader(conn)
		req, err := http.ReadRequest(reader)
		check(err)
		
		url_requested := "." + req.URL.String()
		// https://pkg.go.dev/net/url#URL.String
		fmt.Println(url_requested)
		
		fIn, errIn := os.Open(url_requested)
		defer fIn.Close()
		
		if os.IsNotExist(errIn) {
			fmt.Printf("File not found.\n")
		} else {
			fi, _ := fIn.Stat()
			fmt.Printf("filesize: %d \n", int(fi.Size()))
		}
		
		conn.Close() 
}

// URL *url.URL
func main() {
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", ":12001")
	defer ln.Close()
	
	for {
		conn, _ := ln.Accept()
		handleConnection(conn)
	}
	
	
}
