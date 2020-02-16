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

	data := []string{}

	for _, datum := range strings.Split(string(input), "\n") {
		data = append(data, datum[strings.IndexRune(datum, '@')+2:len(datum)])
	}

	return data
}

func main() {
	fmt.Println(getData("input"))
}
