package main
import (
	"fmt"
	"strings"
)
type talker interface {
	talk() string
}

type martian struct{}

//this function makes the martian type implement the t interface
func (m martian) talk() string {
	return "nack nack"
}

type laser int 

//this function makes the type laser implement the t interface
func (l laser) talk() string {
	return strings.Repeat("poof ", int(l))
}

type rover string

func (r rover) talk() string {
	return "whir whir"
}

func shout(t talker) {
	louder := strings.ToUpper(t.talk())
	fmt.Println(louder)
}

func main() {
	
	var t talker = martian{}
	fmt.Println("a martian says", t.talk())
	shout(t)

	t = laser(3)
	fmt.Println("a laser says", t.talk())
	shout(t)

	t = rover("brennan")
	fmt.Println("a rover says", t.talk())
	shout(t)
}