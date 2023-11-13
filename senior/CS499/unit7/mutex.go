package main

import "sync"

var mu sync.Mutex

func main() {
    mu.Lock()
	 //critical section
	 var x = 1
	 x = x + 1
    mu.Unlock()
}
