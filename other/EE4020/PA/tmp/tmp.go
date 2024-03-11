package main

import (
    "bufio"
    "fmt"
    "strings" 
)

func main() {
    const input = "ScanBytes is a split function for a Scanner that returns each byte as a token.\n"
    scanner := bufio.NewScanner(strings.NewReader(input)) 
    scanner.Split(bufio.ScanBytes)
    count := 0
    for scanner.Scan() {
        count++ 
    }
    fmt.Printf("%d\n", count) 
}