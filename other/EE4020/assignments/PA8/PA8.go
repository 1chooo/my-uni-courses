package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
)


func check (e error){
	if e != nil {
		panic(e)
	}
}

// return the content in the file directory
func listFileDir() []string{
	var filename []string
	// return two values: the files in the directory, error
	entries, err := ioutil.ReadDir("./")
	check(err)

	for _, ent := range entries {
		filename = append(filename, ent.Name())
	}
	return filename
}

// custom not found
func notFound(w http.ResponseWriter, r *http.Request){
	http.Error(w, "File not found.", http.StatusNotFound)
}

func customHandler(w http.ResponseWriter, r *http.Request){
	files := listFileDir()
	filepath := strings.TrimPrefix(r.URL.Path, "/")
	found := false
	for _, filename := range files {
		if filepath == filename {
			h := http.FileServer(http.Dir("."))
			r2 := new(http.Request)
			*r2 = *r
			r2.URL = new(url.URL)
			*r2.URL = *r.URL
			r2.URL.Path = filepath
            // main code looking for specified file in the filesystem
			h.ServeHTTP(w, r2)
			found = true
			break
		}
	}

	if !found {
		notFound(w, r)
	}

}

func main(){
	fmt.Println("Launching server...")
	hd := http.HandlerFunc(customHandler)
	http.Handle("/", hd)
	http.ListenAndServe(":12001", nil)
}
