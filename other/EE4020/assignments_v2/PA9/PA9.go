package main
import "fmt"
import "net/http"
import "os"
func Handler(w http.ResponseWriter, r *http.Request) {
 // check if the requested file is in this folder.
 requestFileName := "." + r.URL.String()
 _, err := os.Stat(requestFileName)
 if (err!=nil || os.IsNotExist(err)){
 	 error404Handler(w, r)
 	 return
 }else{
 	http.ServeFile(w, r, requestFileName)
}
}
func error404Handler(w http.ResponseWriter, r *http.Request) { 
    http.Error(w, "File not found", http.StatusNotFound) 
}
func main() {
 fmt.Println("Launching server...")
 hh := http.HandlerFunc(Handler)
 http.Handle("/", hh)
 http.ListenAndServeTLS(":12007", "server.cer",
 "server.key", nil)
}