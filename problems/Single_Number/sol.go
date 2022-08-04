func singleNumber(nums []int) int {
  num := 0
  for i := 0; i < len(nums); i++ {
    num = num ^ nums[i]
  }
  return nums
}
