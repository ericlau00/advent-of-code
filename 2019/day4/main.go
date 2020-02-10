package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Answer to part 1:", count(1))
	fmt.Println("Answer to part 2:", count(2))
}

func count(part int) int {
	count := 0
	for i := 134792; i <= 675810; i++ {
		if check(digitize(i), part) {
			count++
		}
	}
	return count
}

func digitize(num int) [6]int {
	var digits [6]int
	for i := 0; i < 6; i++ {
		digits[i] = num / int(math.Pow10(6-i-1))
		num %= int(math.Pow10(6 - i - 1))
	}
	return digits
}

func check(num [6]int, part int) bool {
	return increasing(num) && double(num, part)
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

func double(num [6]int, part int) bool {
	digits := make(map[int]int)
	for i := 0; i < 6; i++ {
		if digits[num[i]] == 0 {
			digits[num[i]] = 1
		} else {
			if part == 1 {
				return true
			}
			digits[num[i]]++
		}
	}
	keys := make([]int, len(digits))
	i := 0
	for k := range digits {
		keys[i] = k
		i++
	}
	for k := range keys {
		if digits[keys[k]] == 2 {
			return true
		}
	}

	return false
}
