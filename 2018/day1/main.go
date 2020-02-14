package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	data := strings.Split(string(input), "\n")
	freqs := []int{}

	for i := 0; i < len(data); i++ {
		data[i] = strings.Trim(data[i], "+")
		num, err := strconv.Atoi(data[i])
		if err != nil {
			log.Fatal(err)
		}
		freqs = append(freqs, num)
	}

	var sum int

	for _, num := range freqs {
		sum += num
	}

	fmt.Println("Answer to part 1:", sum)
}
