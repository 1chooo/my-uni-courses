package main

import (
	"bufio"
	"fmt"
	"io"
	"net"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func main() {
	fmt.Println("Launching server...")
	ln, _ := net.Listen("tcp", ":12001")
	for {

		conn, _ := ln.Accept()
		defer ln.Close()
		defer conn.Close()

		reader := bufio.NewReader(conn)
		message, errr := reader.ReadString('\n')
		check(errr)

		//GETTING THE LENGHT->FIRST INFORMATION SENT
		incomingLen, _ := strconv.Atoi(strings.TrimRight(message, "\n"))
		//fmt.Printf("%t", (incomingLen == 1254))

		//CREATING FILE
		file, err := os.Create("whatever.txt")
		check(err)
		writerFile := bufio.NewWriter(file)
		defer file.Close()
		rowCount := 1

		complete_message := ""
		bytesReceived := 0
		for {
			message, errr := reader.ReadString('\n')
			modifiedMessage := fmt.Sprintf("%d %s", rowCount, message)

			bytesReceived += len(message)

			//fmt.Printf("%s",

			if errr != nil {
				if errr == io.EOF {
					break
				}
				check(errr)
			}

			complete_message += modifiedMessage
			if bytesReceived == incomingLen {
				break
			}
			rowCount += 1

		}

		writerFile.WriteString(complete_message)
		writerFile.Flush()
		file.Close()

		file, _ = os.Open("whatever.txt")
		defer file.Close()

		fi, _ := file.Stat()
		writer := bufio.NewWriter(conn)

		newline := fmt.Sprintf("Upload file size: %d,  Output file size: %d\n", incomingLen, int(fi.Size()))
		_, _ = writer.WriteString(newline)
		//check(errw)
		writer.Flush()
		file.Close()
		conn.Close()

	}
}
