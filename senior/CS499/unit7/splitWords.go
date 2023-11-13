package main

import (
	"fmt"
	"strings"
)

func sourceGopher(downstream chan string) {
	for _, v := range []string{"hello world", "a bad apple", "goodbye all"} {
		downstream <- v
	}
	close(downstream)
}

func splitGopher(upstream, downstream chan string) {
	for item := range upstream {
		words := strings.Split(item, " ")
		for i := 0; i < len(words); i++ {
			downstream <- words[i]
	  }
	}
	close(downstream)
}

func printGopher(upstream chan string) {
	for v := range upstream {
		fmt.Println(v)
	}
}

func main() {
	c0 := make(chan string)
   c1 := make(chan string)
   go sourceGopher(c0)
   go splitGopher(c0, c1)
   printGopher(c1)
}