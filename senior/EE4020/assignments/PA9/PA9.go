package main

import (
	"fmt"
	"net/http"
	"os"
)

// Function to handle errors
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	// Define the path f our homeHandler
	path := r.URL.Path[1:]

	// Check if the file exist
	_, err := os.Stat(path)
	if err != nil {
		errorHandler(w, r, http.StatusNotFound)
		return
	} else {
		// Serve the file
		http.ServeFile(w, r, path)
	}
}

func errorHandler(w http.ResponseWriter, r *http.Request, status int) {
	w.WriteHeader(status)
	if status == http.StatusNotFound {
		fmt.Fprintf(w, "404: %s not found", r.URL)
	}
}

func main() {
	http.HandleFunc("/", homeHandler)
	http.ListenAndServeTLS(":12001", "server.cer", "server.key", nil)
}
