/*
Created Date: 2023/11/13
HW: 20
Author: 林群賀
Student Number: 109601003
*/

package main

import "fmt"

func main() {
    trainData := map[string]map[string]int{
        "台北 - 桃園": {"price": 44, "people": 35273},
        "台北 - 新竹": {"price": 116, "people": 21543},
        "台北 - 台中": {"price": 241, "people": 12573},
        "台北 - 嘉義": {"price": 386, "people": 31567},
        "台北 - 高雄": {"price": 544, "people": 52386},
        "台北 - 花蓮": {"price": 284, "people": 44138},
    }

    for location, info := range trainData {
        revenue := info["price"] * info["people"]
        fmt.Printf("%s 在 Q1 的營收為 %d 元\n", location, revenue)
    }
}

