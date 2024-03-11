package main

import "fmt"
import "bufio"
import "net"
// import "io"
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
	defer ln.Close()

	for {
		conn, _ := ln.Accept()
		// defer conn.Close()

		fout, errf := os.Create("whatever.newfile")
		check(errf)
		defer fout.Close()

		fileWriter := bufio.NewWriter(fout)
		reader := bufio.NewReader(conn)
		count := 1
		reachedBytes := 0

		firstmsg, _ := reader.ReadString('\n')
		// fileWriter.WriteString("0")
		// fileWriter.WriteString(firstmsg)
		firstmsg = strings.TrimRight(firstmsg, "\n")
		byteTotal, _ := strconv.Atoi(firstmsg)

		for {
			message, _ := reader.ReadString('\n')
			lineLength := len(message)
			reachedBytes += lineLength

			fileWriter.WriteString(strconv.Itoa(count))
			fileWriter.WriteString(" ")
			fileWriter.WriteString(message)

			count += 1

			if reachedBytes == byteTotal {
				break
			}
		}
		fileWriter.Flush()

		writer := bufio.NewWriter(conn)
		newline := fmt.Sprintf("%d bytes received, %d bytes generated", byteTotal, byteTotal+(count-1)*2)
		_, errw := writer.WriteString(newline)
		check(errw)
		writer.Flush()
		fmt.Printf("Upload file size: %d\nOutput file size: %d\n", byteTotal, byteTotal+(count-1)*2)

		conn.Close()
	}
}

