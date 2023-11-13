package main 
import (
	"fmt"
	"strings"
)

func counts(input string) map[string]int {
	var lowerInput string = strings.ToLower(input)
	var trim1 string = strings.ReplaceAll(lowerInput, ",", "")
	var trim2 string = strings.ReplaceAll(trim1, ".", "")
	var trim3 string = strings.ReplaceAll(trim2, ";", "")
	var trim4 string = strings.ReplaceAll(trim3, "-", "")
	
	tokens := strings.Fields(trim4)

	wordCounts := make(map[string]int)

	for i := 0; i < len(tokens); i++ {
		if value, ok := wordCounts[tokens[i]]; ok {
			wordCounts[tokens[i]] = value + 1
	  	} else {
			wordCounts[tokens[i]] = 1
	  	}
	}
	
	return wordCounts
}

func main() {
	csLewis := "As far as eye could reach he saw nothing but the stems of the great plants about him receding in the violet shade, and far overhead the multiple transparency of huge leaves filtering the sunshine to the solemn splendour of twilight in which he walked. Whenever he felt able he ran again; the ground continued soft and springy, covered with the same resilient weed which was the first thing his hands had touched in Malacandra. Once or twice a small red creature scuttled across his path, but otherwise there seemed to be no life stirring in the wood; nothing to fear—except the fact of wandering unprovisioned and alone in a forest of unknown vegetation thousands or millions of miles beyond the reach or knowledge of man."
	wordCounts := counts(csLewis)
	fmt.Println(wordCounts)
	for key, value := range wordCounts {
		if value > 1 {
			fmt.Println(key, "showed up", value, "times")
		}
		fmt.Println(key, "showed up", value, "times")
  }
}