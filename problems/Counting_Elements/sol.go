countElements(arr []int) int {
  m := make([]int, 1002)
  for i := 0; i < len(arr); i++ {
    m[arr[i]+1] += 1
  }
  count := 0
  for i := 0; i < len(arr); i++ {
    count += m[arr[i]]
    m[arr[i]] = 0
  }
  return count
}

