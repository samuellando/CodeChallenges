func numberOfSteps (num int) int {
    s := 0
	for num > 0 {
		if num % 2 == 0 {
			num /= 2
		} else {
			num -= 1
		}
        s++
	}
    return s
}