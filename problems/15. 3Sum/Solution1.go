import (
    "sort"
    "fmt"
)

func threeSum(nums []int) [][]int {
  // For each number, check following numbers for solutions.
  // O(n+n^2) = O(n^2)

  out := make([][]int,0)
  m := make(map[int]int)
  om := make(map[string]bool)

  for i := 0; i < len(nums); i++ {
    m[nums[i]] = i
  }

  for i := 0; i < len(nums); i++ {
    for j := i+1; j < len(nums); j++ {
      v := -1*(nums[i] + nums[j])
      if _, ok := m[v]; ok && m[v] != i && m[v] != j {
        o := []int{nums[i], nums[j], v}
        sort.Ints(o)
        if !om[fmt.Sprintf("%d%d%d", o[0], o[1], o[2])] {
          out = append(out, o)
          om[fmt.Sprintf("%d%d%d", o[0], o[1], o[2])] = true
        }
      }
    }
  }

  return out
}
