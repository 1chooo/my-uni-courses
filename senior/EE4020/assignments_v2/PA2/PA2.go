package main
import "fmt"
import "os"
import "bufio"

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	// Specify the input file.
	fmt.Printf("Input Name:")
	inputName := ""
	fmt.Scanf("%s\n", &inputName)
	fI, err := os.Open(inputName)
	check(err)
	defer fI.Close()

 	// Specify the output file
	fmt.Printf("Output Name:")
	outputName := ""
	fmt.Scanf("%s\n", &outputName)
	fO, err := os.Create(outputName)
	check(err)
	defer fO.Close()

	// Declare the reader and writer using bufio package.
	scanner := bufio.NewScanner(fI)
	writer := bufio.NewWriter(fO)

	// Adding prepending number to each line of the input file to the output file.
	lineCount := 1
	text := ""
	for scanner.Scan() {
		text = scanner.Text();
		addtext := fmt.Sprintf("%d", lineCount) + " " + text + "\n"

		writer.WriteString(addtext)
		fmt.Printf(addtext)
		lineCount = lineCount + 1
		writer.Flush()
	}
}