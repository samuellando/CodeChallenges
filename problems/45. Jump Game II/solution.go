func jump(nums []int) int {
	reach := make([]int, len(nums))
	reach[len(nums)-1] = 0

	for i := len(nums) - 2; i >= 0; i-- {
		r := -1
		for j := 1; j <= nums[i] && i+j < len(nums); j++ {
			if reach[i+j] != -1 && (1+reach[i+j] <= r || r == -1) {
				r = 1 + reach[i+j]
			}
		}
		reach[i] = r
	}

	fmt.Println(reach)
	return reach[0]
}
