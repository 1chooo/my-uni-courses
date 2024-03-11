// pool.go

package websocket

import "fmt"

type Pool struct {
    Register   chan *Client     // Channel to register new clients
    Unregister chan *Client     // Channel to unregister clients
    Clients    map[*Client]bool // Map of connected clients
    Broadcast  chan Message     // Channel to broadcast messages to all clients
}

func NewPool() *Pool {
    return &Pool{
        Register:   make(chan *Client),
        Unregister: make(chan *Client),
        Clients:    make(map[*Client]bool),
        Broadcast:  make(chan Message),
    }
}

func (pool *Pool) Start() {
    for {
        select {
        case client := <-pool.Register:
            // Add the newly registered client to the pool
            pool.Clients[client] = true
            
            // Log pool size and notify all clients about the new user
            fmt.Println("Size of Connection Pool: ", len(pool.Clients))
            for client := range pool.Clients {
                client.Conn.WriteJSON(
                    Message{Type: 1, Body: "New User Joined..."},
                )
            }
            
        case client := <-pool.Unregister:
            // Remove the client from the pool upon unregistration
            delete(pool.Clients, client)
            
            // Log pool size and notify all clients about the disconnected user
            fmt.Println("Size of Connection Pool: ", len(pool.Clients))
            for client := range pool.Clients {
                client.Conn.WriteJSON(
                    Message{Type: 1, Body: "User Disconnected..."},
                )
            }
            
        case message := <-pool.Broadcast:
            // Broadcast the received message to all clients in the pool
            fmt.Println("Sending message to all clients in Pool")
            for client := range pool.Clients {
                if err := client.Conn.WriteJSON(message); err != nil {
                    fmt.Println(err)
                    return
                }
            }
        }
    }
}
