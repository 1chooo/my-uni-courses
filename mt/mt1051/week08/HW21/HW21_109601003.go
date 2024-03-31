/*
Created Date: 2023/11/13
HW: 21
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func main() {
    // Initialize data
    locations := []string{"台北 - 桃園", "台北 - 新竹", "台北 - 台中", "台北 - 嘉義", "台北 - 高雄", "台北 - 花蓮"}
    prices := []int{44, 116, 241, 386, 544, 284}
    people := [][]int{
        {35273, 21543, 12573, 31567, 52386, 44138},
        {25673, 55728, 31245, 33278, 51342, 22464},
        {21345, 22179, 32189, 36296, 33106, 43278},
        {53278, 32785, 43167, 21367, 44579, 32685},
    }

    // Initialize revenue as a 2D slice
    revenue := make([][]int, len(locations))
    for i := range revenue {
        revenue[i] = make([]int, len(people))
    }

    // Calculate revenue
    for i := range locations {
        for j := range people {
            revenue[i][j] = prices[i] * people[j][i]
        }
    }

    // Print revenue
    fmt.Println("revenue:", revenue)

    // Print revenue for each location
    for i := range locations {
        fmt.Printf("%s 路線在 Q1 - Q4 的營收分別為 %v 元\n", locations[i], revenue[i])
    }
}
