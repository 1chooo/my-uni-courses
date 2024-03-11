// Date: 2023/09/18
// HW: 02
// Author: 林群賀
// Student Number: 109601003

package main

import (
	"fmt"
	"math"
)

type QuestionOne struct {
	Bottom float64
	Height float64
}

func (q *QuestionOne) GetArea() float64 {
	area := (q.Bottom * q.Height) / 2
	return area
}

type QuestionTwo struct {
	Radius float64
	PI     float64
}

func (q *QuestionTwo) GetArea() float64 {
	area := math.Pow(q.Radius, 2) * q.PI
	return math.Round(area*100) / 100
}

type QuestionThree struct {
	Triangle1Bottom float64
	Triangle1Height float64

	Triangle2Bottom float64
	Triangle2Height float64

	Triangle3Bottom float64
	Triangle3Height float64
}

func (q *QuestionThree) GetTriangleArea(bottom, height float64) float64 {
	area := (bottom * height) / 2
	return area
}

func (q *QuestionThree) GetTotalArea() float64 {
	area1 := q.GetTriangleArea(q.Triangle1Bottom, q.Triangle1Height)
	area2 := q.GetTriangleArea(q.Triangle2Bottom, q.Triangle2Height)
	area3 := q.GetTriangleArea(q.Triangle3Bottom, q.Triangle3Height)

	return math.Round((area1 + area2 + area3) * 100) / 100
}

type QuestionFour struct {
	ExternalRadius float64
	InternalRadius float64
	Height         float64
	PI             float64
}

func (q *QuestionFour) GetExternalArea() float64 {
	area := math.Pow(q.ExternalRadius, 2)
	return area
}

func (q *QuestionFour) GetInternalArea() float64 {
	area := math.Pow(q.InternalRadius, 2)
	return area
}

func (q *QuestionFour) GetTopArea() float64 {
	area := q.GetExternalArea() - q.GetInternalArea()
	return area
}

func (q *QuestionFour) GetVolume() float64 {
	volume := q.GetTopArea() * q.PI * q.Height
	return math.Round(volume*100) / 100
}

func main() {
	questionOne := QuestionOne{Bottom: 2.5, Height: 3.6}
	questionTwo := QuestionTwo{Radius: 2.8 / 2, PI: 3.14159}
	questionThree := QuestionThree{
		Triangle1Bottom: 1.6,
		Triangle1Height: 2.2,
		Triangle2Bottom: 2.6,
		Triangle2Height: 3.2,
		Triangle3Bottom: 3.6,
		Triangle3Height: 4.5,
	}
	questionFour := QuestionFour{
		ExternalRadius: 3.2 / 2,
		InternalRadius: 1.5 / 2,
		Height:         6.8,
		PI:             3.14159,
	}

	areaOne := questionOne.GetArea()
	areaTwo := questionTwo.GetArea()
	areaThree := questionThree.GetTotalArea()
	areaFour := questionFour.GetVolume()

	fmt.Println("1.", areaOne)
	fmt.Println("2.", areaTwo)
	fmt.Println("3.", areaThree)
	fmt.Println("4.", areaFour)
}
