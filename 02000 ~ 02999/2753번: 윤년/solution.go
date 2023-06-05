// 백준 2753번 윤년
package main

import (
	"fmt"
)

func main() {
	var year int
	fmt.Scanln(&year)

	if year%400 == 0 || (year%4 == 0 && year%100 != 0) {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
