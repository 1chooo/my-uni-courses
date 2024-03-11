// websocket.go 

package websocket

import (
    "log"
    "net/http"

    "github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
    ReadBufferSize:  1024, // Size of the read buffer
    WriteBufferSize: 1024, // Size of the write buffer
    CheckOrigin: func(r *http.Request) bool { 
        return true 
    }, // Function to check request origin
}

func Upgrade(w http.ResponseWriter, r *http.Request) (*websocket.Conn, error) {
    conn, err := upgrader.Upgrade(w, r, nil)
    if err != nil {
        log.Println(err)
        return nil, err
    }

    return conn, nil
}