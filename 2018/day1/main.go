package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func getFrequencies(data []string) []int {
	freqs := []int{}

	for i := 0; i < len(data); i++ {
		data[i] = strings.Trim(data[i], "+")
		num, err := strconv.Atoi(data[i])
		if err != nil {
			log.Fatal(err)
		}
		freqs = append(freqs, num)
	}

	return freqs
}

func solvePartOne(freqs []int) int {
	sum := 0

	for _, num := range freqs {
		sum += num
	}

	return sum
}

func solvePartTwo(freqs []int) int {
	m := make(map[int]bool)
	sum := 0

	for !m[sum] {
		for _, num := range freqs {
			m[sum] = true
			sum += num
			if m[sum] {
				break
			}
		}
	}
	return sum
}

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	data := strings.Split(string(input), "\n")
	freqs := getFrequencies(data)

	fmt.Println("Answer to part 1:", solvePartOne(freqs))
	fmt.Println("Answer to part 2:", solvePartTwo(freqs))
}
