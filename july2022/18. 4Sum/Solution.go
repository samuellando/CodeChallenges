import (
  "fmt"
  "sort"
)


func fourSum(nums []int, target int) [][]int {
  out := make([][]int, 0)
  search := make(map[int]int)
  outMap := make(map[string]bool)

  for i := 0; i < len(nums); i++ {
    search[nums[i]] = i
  }

  for i := 0; i < len(nums); i++ {
    for j := i + 1; j < len(nums); j++ {
      for k := j + 1; k < len(nums); k++ {
        v := target - (nums[i] + nums[j] + nums[k])
        if h, ok := search[v]; ok && h != i && h != j && h != k  {
          o := []int{nums[i], nums[j], nums[k], v}
          sort.Ints(o)
          s := fmt.Sprintf("%d%d%d%d", o[0], o[1], o[2], o[3])
          if !outMap[s] {
            outMap[s] = true
            out = append(out, o)
          }
        }
      }
    }
  }

  return out
}

