package main
import (
	"fmt"
	"math/rand"
	"time"
	"os"
   "os/exec"
   "runtime"
)

const (
	width = 140
	height = 35
)

type Universe [][]bool

func NewUniverse() Universe {
	toReturn := make([][]bool, height)
	for i := range toReturn {
		toReturn[i] = make([]bool, width)
	}
	return toReturn
}

func (u Universe) Show() {
	for i := 0; i < width + 2; i++ {
		fmt.Printf("-")
	}
	fmt.Printf("\n")
	for row := range u {
		fmt.Printf("-")
		for col := range u[row] {
			if u[row][col] {
				fmt.Printf("*")
			} else {
				fmt.Printf(" ")
			}
		}
		fmt.Printf("-")
		fmt.Printf("\n")
	}
	for i := 0; i < width + 2; i++ {
		fmt.Printf("-")
	}
	fmt.Printf("\n")
}

func (u Universe) Seed() {
	rand.Seed(time.Now().UnixNano())
	for row := range u {
		for col := range u[row] {
			randomFrac := rand.Float64()
			if randomFrac < 0.77 {
				u[row][col] = true
			} else {
				u[row][col] = false
			}
		}
	}
}

func (u Universe) Alive(row, col int) bool {
	row = (row + height) % height
	//fmt.Printf("row = %v\n", row)
	col = (col + width) % width
	//fmt.Printf("col = %v\n", col)
	return u[row][col]
}

func (u Universe) Neighbors(x, y int) int {
	neighborCnt := 0
	if u.Alive(x + 1, y - 1) {
		neighborCnt++
	}
	if u.Alive(x + 1, y) {
		neighborCnt++
	}
	if u.Alive(x + 1, y + 1) {
		neighborCnt++
	}

	if u.Alive(x - 1, y + 1) {
		neighborCnt++
	}
	if u.Alive(x - 1, y) {
		neighborCnt++
	}
	if u.Alive(x - 1, y - 1) {
		neighborCnt++
	}

	if u.Alive(x, y + 1) {
		neighborCnt++
	}
	if u.Alive(x, y - 1) {
		neighborCnt++
	}
	return neighborCnt
}

func (u Universe) Next(x, y int) bool {
	neighbors := u.Neighbors(x, y)
	if u.Alive(x, y) {
		//the cell in question is alive originally
		if neighbors == 2 || neighbors == 3 {
			//cell stays alive
			return true
		} else {
			//cell dies
			return false
		}
	} else {
		//the cell in question is dead originally
		if neighbors == 3 {
			//revive the cell cause it has exactly 3 neighbors
			return true
		} else {
			//otherwise stays dead
			return false
		}
	}
}

//returns the universe one cycle after the universe state a
//read through a and dont change it
//update b and return it
func Step(a Universe) Universe {
	//make a copy of the universe
	b := make(Universe, len(a))
	for i := range a {
		b[i] = make([]bool, len(a[i]))
		copy(b[i], a[i])
	}

	//update the state of all spots in universe
	for row := range a {
		for col := range a[row] {
			b[row][col] = a.Next(row, col)
		}
	}
	return b
}

func clearScreen() {
	switch runtime.GOOS {
	case "windows":
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	case "linux", "darwin":
		fmt.Print("\033[2J\033[H")
	default:
		fmt.Print("Unsupported platform")
	}
}

func main() {
	animationDelay := time.Duration(.05 * float64(time.Second))
	numIters := 500
	//print out starting info
	fmt.Println("This is Conways Game of Life with a random seed\n")
	//make new universe
	board := NewUniverse()
	board.Seed()
	//print out starting universe
	clearScreen()
	board.Show()
	//sleep 1 unit long
	time.Sleep(2 * animationDelay)
	//for i < numIters
	for i := 1; i < numIters + 1; i++ {
		//step
		board = Step(board)
		//sleep 1 unit
		time.Sleep(animationDelay)
		//wipe screen 
		clearScreen()
		//show
		board.Show()
	}
}