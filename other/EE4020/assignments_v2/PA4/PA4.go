package main

import "fmt"
import "bufio"
import "net"
import "io"
import "os"
import "strconv"
import "strings"

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

	fout, errf := os.Create("whatever.txt")
	check(errf)
	defer fout.Close()
	fileWriter := bufio.NewWriter(fout)
	reader := bufio.NewReader(conn)
	count := 1
	fileLength := 0

	firstmsg, _ := reader.ReadString('\n')
	// fileWriter.WriteString("0")
	// fileWriter.WriteString(firstmsg)
	firstmsg = strings.TrimRight(firstmsg, "\n")
	byteTotal, _ := strconv.Atoi(firstmsg)
	// fmt.Printf("%s %d\n\n", firstmsg, byteTotal)
	for {
		message, errr := reader.ReadString('\n')
		if errr != nil && errr != io.EOF {
			break
		}

		byteCount := len(message)
		fileLength += byteCount
		// fmt.Printf("%d:%s",count, message)
		// fmt.Printf("%d %d\n", byteCount, fileLength)

		fileWriter.WriteString(strconv.Itoa(count))
		fileWriter.WriteString(message)

		count += 1

		if fileLength == byteTotal {
			break
		}

		if errr != nil {
			break
		}
	}
	fileWriter.Flush()
	// fmt.Printf("read complete\n")

	writer := bufio.NewWriter(conn)
	newline := fmt.Sprintf("original file size: %d\tnew file size: %d\n", byteTotal, byteTotal+count)
	_, errw := writer.WriteString(newline)
	check(errw)
	writer.Flush()
}
