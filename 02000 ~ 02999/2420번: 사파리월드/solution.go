// 백준 2420번 사파리월드 
package main

import (
	"fmt"
)

func main() {
	var N, M int
	fmt.Scanln(&N, &M)

	if N > M {
		fmt.Println(N - M)
	} else{
		fmt.Println(M - N)
	}
}
