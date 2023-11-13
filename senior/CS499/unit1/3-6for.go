package main
import(
	"fmt"
	"time"
)

func main() {
	var count = 5

	for count > 0 {
		fmt.Println(count)
		time.Sleep(time.Second)
		count--
	}
	fmt.Println("Were going on a trip in your favorite rocket ship blasting through the sky little einsteins")
}