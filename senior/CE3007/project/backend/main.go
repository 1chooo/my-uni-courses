// main.go

package main

import (
    "fmt"
    "net/http"

    "github.com/1chooo/socket-programming/pkg/websocket"
)

func serveWs(pool *websocket.Pool, w http.ResponseWriter, r *http.Request) {
    fmt.Println("WebSocket Endpoint Hit")
    conn, err := websocket.Upgrade(w, r)
    if err != nil {
        fmt.Fprintf(w, "%+v\n", err)
    }

    // Create a new client using the WebSocket connection and pool
    client := &websocket.Client{
        Conn: conn,
        Pool: pool,
    }

    // Register the new client to the pool
    pool.Register <- client
    // Start reading messages from the WebSocket connection
    client.Read()
}

func setupRoutes() {
    // Create a new WebSocket pool
    pool := websocket.NewPool()
    // Start the WebSocket pool in a separate goroutine
    go pool.Start()

    // Define a WebSocket endpoint and specify the handler function
    http.HandleFunc(
        "/ws", 
        func(w http.ResponseWriter, r *http.Request) {
            serveWs(pool, w, r)
        },
    )
}

func main() {
    fmt.Println("Online Anonymous Multi-User Chat App v0.01")
    fmt.Println("Server Running on Port 8080...")
    setupRoutes()
    http.ListenAndServe(":8080", nil)
}
