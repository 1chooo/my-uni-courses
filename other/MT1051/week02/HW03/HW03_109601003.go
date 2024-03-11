// Date: 2023/09/18
// HW: 03
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
	"math"
)

type HomeworkThree struct {
	PointA struct {
		X float64
		Y float64
	}
	PointB struct {
		X float64
		Y float64
	}
}

func (h *HomeworkThree) GetPointInfo() {
	fmt.Print("x1 = ")
	fmt.Scan(&h.PointA.X)
	fmt.Print("y1 = ")
	fmt.Scan(&h.PointA.Y)
	fmt.Print("x2 = ")
	fmt.Scan(&h.PointB.X)
	fmt.Print("y2 = ")
	fmt.Scan(&h.PointB.Y)
}

func (h *HomeworkThree) GetDistance() float64 {
	x := h.PointA.X - h.PointB.X
	y := h.PointA.Y - h.PointB.Y
	distance := math.Sqrt(x*x + y*y)
	return math.Round(distance*100) / 100
}

func main() {
	homeworkThree := HomeworkThree{}
	homeworkThree.GetPointInfo()
	distance := homeworkThree.GetDistance()
	fmt.Printf("Distance with input value: %.2f\n", distance)
}
