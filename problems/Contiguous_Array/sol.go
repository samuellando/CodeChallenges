func findMaxLength(nums []int) int {
	hash := make([]int, 2*50000 + 1)
    
    for i := 0; i < len(hash); i++ {
        hash[i] = -1
    }
    
	max := 0
	sum := 0
	for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            sum --
        } else {
            sum++
        }
        
        if sum == 0 || (hash[sum + 50000] != -1 && i - hash[sum + 50000] > max)  {
            max = i - hash[sum + 50000]
        } else {
            if hash[sum + 50000] == -1 {
                hash[sum + 50000] = i
            }
        }
	}
	return max
}