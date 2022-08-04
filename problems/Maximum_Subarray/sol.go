const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func maxSubArray(nums []int) int {
  // I suck at dynamic programming.
  currentSum := nums[0]
  bestSum := nums[0]
  for i := 1; i < len(nums); i++ {
    if currentSum + nums[i] > nums[i] {
      currentSum = currentSum + nums[i]
    } else {
      currentSum = nums[i]
    }
    if currentSum > bestSum {
      bestSum = currentSum
    }
  }

  return bestSum
}

