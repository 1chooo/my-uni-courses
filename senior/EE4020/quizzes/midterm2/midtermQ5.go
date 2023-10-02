// To complete the game client, extend the code to exam2-p13-5.go such that it connects to the server running on port 12000, sends “play\n”, receives a line of message from the server, prints the message on the screen. Then, repeatedly prompts the user for a guess, sends the number in one line (+’\n’ at the end of the number), receives a line of message from the server and prints the line of message on the screen until the server response is “Bingo\n”.
// Extend the code to exam2-13-4.go such that it connects to the server running on port 12000, sends “play\n”, receives a line of message from the server, prints the message on the screen. Then, prompts the user for a guess, sends the number in one line (+’\n’ at the end of the number), receives a line of message from the server, prints the line of message on the screen, and then closes the connection.
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// Connect to the server running on port 12000
	conn, err := net.Dial("tcp", ":12000")
	if err != nil {
		fmt.Println("Error connecting:", err)
		os.Exit(1)
	}

	// Send the string "play\n" to the server
	writer := bufio.NewWriter(conn)
	writer.WriteString("play\n")
	writer.Flush()

	// Read a line of message from the server
	reader := bufio.NewReader(conn)
	message, err := reader.ReadString('\n')
	fmt.Println(message)

	// While the server response is not "Bingo\n", keep prompting the user for a guess
	for message != "Bingo\n" {
		fmt.Print("Enter a guess: ")
		guess := 0
		fmt.Scanf("%d", &guess)
		// Send the guess to the server and see if it's correct
		writer = bufio.NewWriter(conn)
		writer.WriteString(fmt.Sprintf("%d\n", guess))
		writer.Flush()
		message, err = reader.ReadString('\n')
		fmt.Println(message)
	}

	// // Prompt the user for a guess
	// fmt.Print("Enter a guess: ")
	// guess := 0
	// fmt.Scanf("%d", &guess)

	// // Send the guess to the server
	// writer = bufio.NewWriter(conn)
	// writer.WriteString(fmt.Sprintf("%d\n", guess))
	// writer.Flush()
	// message, err = reader.ReadString('\n')
	// fmt.Println(message)

	// Close the connection
	conn.Close()
}
