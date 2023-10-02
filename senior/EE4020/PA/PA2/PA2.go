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

	fmt.Printf("Output filename: ") 
	out_text := ""
	fmt.Scanf("%s", &out_text)

	out_file, err := os.Create(out_text) 
	check(err)
	defer out_file.Close() 
	writer := bufio.NewWriter(out_file)

	var cnt int = 0
	scanner := bufio.NewScanner(in_file) 
	for scanner.Scan() {
		cnt = cnt + 1
		_, _ = writer.WriteString(fmt.Sprintf("%d %s\n", cnt, scanner.Text()))
	}

	in_file.Close() 
	//out_file.Close() 
	writer.Flush()	
}