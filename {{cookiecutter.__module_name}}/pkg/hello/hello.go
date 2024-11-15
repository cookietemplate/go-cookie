package hello

import "fmt"

func SayHello(name string) string {
	fmt.Println("In function SayHello")
	return fmt.Sprintf("Hello, %s!", name)
}
