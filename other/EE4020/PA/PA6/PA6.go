package main

import "fmt"
import "bufio"
import "net"
import "os"
import "strings"
import "strconv"
import "time"

func check(e error) {
   	if e != nil {
		panic(e) 
	}
}


func handleConnection(c net.Conn) {
	// receive fize size and print it
	reader := bufio.NewReader(c) 
	received_size, errr := reader.ReadString('\n') 
    received_size = strings.TrimRight(received_size, "\n")
	check(errr)
	tmp, err:= strconv.Atoi(received_size)
	fmt.Printf("Upload file size: %s \n", received_size)

	// receive the file and generate "whatever.txt"
	out_file, err := os.Create("whatever.txt")
	check(err)
	defer out_file.Close() 
	output_writer := bufio.NewWriter(out_file)

	var cnt int = 0
	var file_size = 0
	var current_bytes = 0
	
	for {
		cnt = cnt + 1
		message, errr := reader.ReadString('\n') 
		check(errr)

		_, _ = output_writer.WriteString(fmt.Sprintf("%d %s", cnt, message))
		file_size = file_size + len(message) + len(strconv.Itoa(cnt)) + 1
		current_bytes = current_bytes + len(message)

		
		if (current_bytes >= tmp) {
			break
		}
	}

	output_writer.Flush()
	client_writer := bufio.NewWriter(c)
	newline := fmt.Sprintf("%s bytes received, %d bytes file generated \n", received_size, file_size) 
	_, errw := client_writer.WriteString(newline)
	check(errw)
	client_writer.Flush()

	fmt.Printf("Output file size: %d \n", file_size)
	time.Sleep(5 * time.Second) 
}

func main(){
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", ":12003")
	defer ln.Close()

	for{
		conn, _ := ln.Accept()
		defer conn.Close()

		go handleConnection(conn) 
	}
}