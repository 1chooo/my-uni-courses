/*
Created Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
*/

package main

import "fmt"
import "net"
import "bufio"
import "os"

func main() {
    service := "localhost:1200"
    conn, err := net.Dial("tcp", service)

    if err != nil {
        fmt.Println("Error connecting:", err)
        return
    }
    defer conn.Close()

    scanner := bufio.NewScanner(conn)
    go func() {
        for scanner.Scan() {
            fmt.Println(scanner.Text())
        }
    }()

    reader := bufio.NewReader(os.Stdin)
    for {
        fmt.Print("Enter message: ")
        text, _ := reader.ReadString('\n')
        conn.Write([]byte(text))
    }
}
