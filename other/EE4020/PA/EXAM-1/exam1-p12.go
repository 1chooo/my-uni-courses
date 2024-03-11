package main

import "fmt"
import "os"
import "bufio"

func check(e error) {
	if e != nil {
		panic(e) 
	}
}

func main() {
	fmt.Printf("Input filename: ") 
	in_text := ""
	fmt.Scanf("%s", &in_text)

	in_file, err := os.Open(in_text) 
	check(err)

	scanner := bufio.NewScanner(in_file) 
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	in_file.Close() 
}