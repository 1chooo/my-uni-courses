// Date: 2023/09/18
// HW: 03
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
)

type Census struct {
	InitPeople      int
	YearDays        int
	Years           int
	HoursPerDay     int
	MinutesPerHour  int
	SecondsPerMinute int

	BornRate        int
	DieRate         int
	ImmigratingRate int
}

func NewCensus() *Census {
	census := &Census{
		InitPeople:      342032486,
		YearDays:        365,
		Years:           5,
		HoursPerDay:     24,
		MinutesPerHour:  60,
		SecondsPerMinute: 60,

		BornRate:        7,
		DieRate:         13,
		ImmigratingRate: 45,
	}
	return census
}

func (c *Census) GetTotalTime() int {
	totalTime := c.YearDays * c.Years * c.HoursPerDay * c.MinutesPerHour * c.SecondsPerMinute
	return totalTime
}

func (c *Census) GetBornPeople() int {
	totalTime := c.GetTotalTime()
	bornPeople := totalTime / c.BornRate
	return bornPeople
}

func (c *Census) GetDiePeople() int {
	totalTime := c.GetTotalTime()
	diePeople := totalTime / c.DieRate
	return diePeople
}

func (c *Census) GetImmigratingPeople() int {
	totalTime := c.GetTotalTime()
	immigratingPeople := totalTime / c.ImmigratingRate
	return immigratingPeople
}

func (c *Census) GetTotalPeople() int {
	totalPeople := c.InitPeople + c.GetBornPeople() + c.GetImmigratingPeople() - c.GetDiePeople()
	return totalPeople
}

func main() {
	census := NewCensus()
	initPeople := census.InitPeople
	totalPeople := census.GetTotalPeople()

	fmt.Println("Jan, 01:", initPeople)
	fmt.Println("Five years later, Dec, 31:", totalPeople)
}
