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

	fmt.Printf("Input file name : ")
	filepath := ""
	fmt.Scanf("%s", &filepath)
	conn, errc := net.Dial("tcp", "127.0.0.1:12007")//tcp:is a kind of transfer
	//127.0.0.1 is the easiest one for our own computer
	check(errc)
	defer conn.Close()
	filepath = "./" + filepath
	fi, errfi := os.Stat(filepath)
	check(errfi)
	size := fi.Size()

	writer := bufio.NewWriter(conn)
	newline := fmt.Sprintf("%d\n", size)
	_, errw := writer.WriteString(newline)
	check(errw)

	f, errfo := os.Open(filepath)
	check(errfo)

	scanner_f := bufio.NewScanner(f)//scan from file
	for scanner_f.Scan(){
		newtext := fmt.Sprintf("%s\n", scanner_f.Text())
		_, errw := writer.WriteString(newtext)
		check(errw)
	}
	writer.Flush()

	scanner_s := bufio.NewScanner(conn)//scan from server
	if scanner_s.Scan() {
		fmt.Printf("Server says: %s\n", scanner_s.Text())
 	}
}
