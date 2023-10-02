package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strconv"
	"io"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// get filename and open the file
	iFile := ""

	fmt.Printf("Please input the upload filename: ")
	fmt.Scanf("%s", &iFile)
	fIn, errIn := os.Open(iFile)
	fi, _ := fIn.Stat()

	defer fIn.Close()
	check(errIn)

	// open connection
	conn, errc := net.Dial("tcp", "127.0.0.1:12001")
	check(errc)
	defer conn.Close()

	// declare file scanner
	docReader := bufio.NewReader(fIn)
	writer := bufio.NewWriter(conn)
	complete_message := ""
	// first send the length of the string
	writer.WriteString(strconv.Itoa(int(fi.Size())) + "\n")
	writer.Flush()
	fmt.Printf("Send a string of %d bytes\n", int(fi.Size()))

	// append to the message and then send to the server
	for {
	    message, errr := docReader.ReadString('\n')
	    if errr != nil {
		if errr == io.EOF {
		    break
		}
		check(errr)
	    }
	    
	    complete_message += message
            
	}
	fmt.Printf(complete_message)
	writer.WriteString(complete_message)
	writer.Flush()
	

	// OK until here - but not received
	serverScanner := bufio.NewScanner(conn)
	if serverScanner.Scan() {
		fmt.Printf("Server replies %s\n", serverScanner.Text())
	}
}

