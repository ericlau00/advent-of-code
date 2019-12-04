package main

import (
	"fmt"
	"math"
)

func main() {
	count := 0
	for i := 134792; i <= 675810; i++ {
		if check(digitize(i)) {
			count++
		}
	}
	fmt.Println("Answer to part 1:", count)

}

func digitize(num int) [6]int {
	var digits [6]int
	for i := 0; i < 6; i++ {
		digits[i] = num / int(math.Pow10(6-i-1))
		num %= int(math.Pow10(6 - i - 1))
	}
	return digits
}

func check(num [6]int) bool {
	return increasing(num) && double(num)
}


func increasing(num [6]int) bool {
	max := 0
	for i := 0; i < 6; i++ {
		if num[i] > max {
			max = num[i]
		}
		if num[i] < max {
			return false
		}
	}
	return true
}

func double(num [6]int) bool {
	digits := make(map[int]int)
	for i := 0; i < 6; i++ {
		if(digits[num[i]] == 0) {
			digits[num[i]] = 1
		} else {
			return true
		}
	}
	return false
}