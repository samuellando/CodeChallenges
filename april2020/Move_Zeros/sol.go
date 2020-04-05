func moveZeroes(nums []int)  {
  n := 0 // Number of zeros.
  insertP := 0
  for i := 0; i < len(nums); i++ {
    if nums[i] != 0 {
      nums[insertP] = nums[i]
      insertP++
    } else {
      n++
    }
  }
  for i := 0; i < n; i++ {
    nums[len(nums) - 1 - i] = 0
  }
}
