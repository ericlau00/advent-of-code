package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func getData(file string) []string {
	input, err := ioutil.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	return strings.Split(string(input), "\n")
}

func check(id string, num int) bool {
	for _, char := range id {
		if strings.Count(id, string(char)) == num {
			return true
		}
	}
	return false
}

func checksum(data []string) int {
	numTwo := 0
	numThree := 0
	for _, id := range data {
		if check(id, 2) {
			numTwo++
		}
		if check(id, 3) {
			numThree++
		}
	}
	return numTwo * numThree
}

func main() {
	data := getData("input")
	fmt.Println("Answer to part 1:", checksum(data))
}
