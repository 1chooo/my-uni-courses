package main

import "fmt"
import "os"
import "bufio"
import "net"
import "io/ioutil"
import "strconv"

func check(e error) {
	if e != nil {
		panic(e) 
	}
}

func main(){
	conn, errc := net.Dial("tcp", "127.0.0.1:12000") 
   	check(errc)
   	defer conn.Close()

   	fmt.Printf("Input filename: ") 
	in_text := ""
	fmt.Scanf("%s", &in_text)

	in_file, err := os.Open(in_text) 
	check(err)

   	// get the file size
   	stat, err := in_file.Stat()
   	check(err)
   	fmt.Printf("Send the file size first: %d\n", stat.Size())

   	// Send the file size first
    writer := bufio.NewWriter(conn)
    _, errw := writer.WriteString(strconv.Itoa(int(stat.Size())) + "\n")
   	check(errw)

   	// Send the file later
   	dat, err := ioutil.ReadFile(in_text)
    check(err)	
    _, errw = writer.Write(dat) 
   	check(errw)
	writer.Flush()

	// Print whatever returns
	scanner := bufio.NewScanner(conn) 
   	if scanner.Scan() { 
    	fmt.Printf("Server says: %s\n", scanner.Text())
   	}

	in_file.Close() 	
}