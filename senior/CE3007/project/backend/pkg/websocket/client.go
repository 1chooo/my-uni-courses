// pkg/websocket/client.go

package websocket

import (
    "fmt"
    "log"
    // "sync"

    "github.com/gorilla/websocket"
)

type Client struct {
    ID   string          // Unique identifier for the client
    Conn *websocket.Conn // WebSocket connection of the client
    Pool *Pool           // Pool reference where the client is registered
}


type Message struct {
    Type int    `json:"type"` // Type of the message
    Body string `json:"body"` // Body content of the message
}


func (c *Client) Read() {
    defer func() {
        c.Pool.Unregister <- c // Unregister client from the pool
        c.Conn.Close()         // Close the client's WebSocket connection
    }()

    for {
        messageType, p, err := c.Conn.ReadMessage() // Read the incoming WebSocket message
        if err != nil {
            log.Println(err)
            return
        }

        message := Message{Type: messageType, Body: string(p)} // Create a message from the received data
        c.Pool.Broadcast <- message                           // Broadcast the received message to all clients
        fmt.Printf("Message Received: %+v\n", message)        // Print the received message
    }
}

