/*
The classical Dining philosophers problem.

Implemented with chopSticks (aka chopsticks) as mutexes.
*/

package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)
//redifining a chopStick as a mutex
type ChopStick struct{ sync.Mutex }

// a philosopher struct that has a 
type Philosopher struct {
	id                  int
	leftChopStick, rightChopStick *ChopStick
}

// Endlessly dine.
// Goes from thinking to hungry to eating and starts over.
// Adapt the pause values to increased or decrease contentions
// around the chopSticks.
func (p Philosopher) dine() {
	say("thinking", p.id)
	randomPause(2)

	say("hungry", p.id)
	p.leftChopStick.Lock()
	p.rightChopStick.Lock()

	say("eating", p.id)
	randomPause(5)

	p.rightChopStick.Unlock()
	p.leftChopStick.Unlock()

	p.dine()
}

func randomPause(max int) {
	time.Sleep(time.Millisecond * time.Duration(rand.Intn(max*1000)))
}

//special print function
func say(action string, id int) {
	fmt.Printf("#%d is %s\n", id, action)
}

//just seeds the random time
func init() {
	// Random seed
	rand.Seed(time.Now().UTC().UnixNano())
}

func main() {
	// How many philosophers and chopSticks
	count := 5

	// Create chopSticks
    //john makes a slice of pointers to chopStick mutexes
	chopSticks := make([]*ChopStick, count)
    //make n chopSticks
	for i := 0; i < count; i++ {
		//create new mutex
        chopSticks[i] = new(ChopStick)
	}

	// Create philospoher, assign them 2 chopSticks and send them to the dining table
	philosophers := make([]*Philosopher, count)
	for i := 0; i < count; i++ {
		if i > (i + 1) % count {
			philosophers[i] = &Philosopher{
				id: i, leftChopStick: chopSticks[(i + 1) % count], rightChopStick: chopSticks[i]
			}
		}
		philosophers[i] = &Philosopher{
			id: i, leftChopStick: chopSticks[i], rightChopStick: chopSticks[(i+1)%count]
		}
      //john spin up a go routine with the philosopher
		go philosophers[i].dine()
	}

	// Wait endlessly while they're dining
	endless := make(chan int)       
    // john apparently if you never catch a channels value it waits endlessly
	<-endless
}