package main

import (
	"fmt"
)

func productExceptSelf(nums []int) []int {
	r := make([]int, len(nums))
	l := make([]int, len(nums))
	rp := 1
	lp := 1

	for i := 0; i < len(nums); i++ {
		r[i] = rp * nums[i]
		rp = r[i]
		l[len(nums) - 1 - i] = lp * nums[len(nums) - 1 - i]
		lp = l[len(nums) - 1 - i]
	}

	sol := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		if i > 0 && i < len(nums) - 1 {
			sol[i] = r[i - 1]*l[i + 1] 
			continue
		} 
		if i > 0 {
			sol[i] = r[i - 1]
		}
		if i < len(nums) - 1 {
			sol[i] = l[i + 1]
		}
	}

	return sol
}

func main() {
	fmt.Println(productExceptSelf([]int{1,2}))
}