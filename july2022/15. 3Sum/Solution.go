import (
    "sort"
)

func threeSum(nums []int) [][]int {
  // For each number, check following numbers for solutions.
  // [-1,0,1,2-1,-4]
  // O(n(n-1)(n-2)) = O(n^3)

  out := make([][]int,0)

  for i := 0; i < len(nums); i++ {
    for j := i+1; j < len(nums); j++ {
      for k := j+1; k < len(nums); k++ {
        if nums[i] + nums[j] + nums[k] == 0 {
          o := []int{nums[i], nums[j],nums[k]}
          out = append(out, o)
        }
      }
    }
  }

  // Remove duplicates.

  // O(n^2log(n))

  for i := 0; i < len(out); i++ {
    sort.Ints(out[i])
  }

  // O(n^2)

  for i := 0; i < len(out); i++ {
    for j := i + 1; j < len(out); j++ {
      for k := 0; k < 3; k++ {
        if out[i][k] != out[j][k] {
          break
        }
        if k == 2 {
          out = append(out[:j], out[j+1:]...)
          j--
        }
      }
    }
  }

  return out
}
