/*
Created Date: 2023/12/11
HW: 35
Author: 林群賀
Student Number: 109601003
*/

package main

import (
	"fmt"
	"net/url"
	"os/exec"
	"strings"
)

func main() {
	cmd := exec.Command("open", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	cmd.Start()

	var address string
	fmt.Print("Please input your address: ")
	fmt.Scanln(&address)

	address = url.QueryEscape(address)
	url := fmt.Sprintf("https://google.com/maps/place/%s", address)

	parts := strings.Split(url, " ")
	cmd = exec.Command("open", parts[0], parts[1])
	cmd.Start()
}
