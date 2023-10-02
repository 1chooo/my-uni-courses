package main
import "fmt"
import "net/http"

import "os"

func customFileHandler(w http.ResponseWriter, r *http.Request) {
	_, err := os.Open("."+r.URL.String())
	if (err != nil){
		// Customized response
		fmt.Fprintln(w, "File not found.")
	}else{
		// Use standard library to help send the response.
		route := http.Dir(".")
		fs := http.FileServer(route)
		fs.ServeHTTP(w, r)
	}
	
}
func main() {
	fmt.Println("Launching server...")

	// Customized no file handler
	nf := http.HandlerFunc(customFileHandler)
	http.Handle("/", nf)

	http.ListenAndServe(":12007", nil)
}