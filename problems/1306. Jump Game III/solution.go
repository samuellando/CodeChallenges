func bfs(arr []int, checked []bool, start int) bool {

  checked[start] = true

  f := start + arr[start]
  b := start - arr[start]

  if arr[start] == 0 {
    return true
  } 

  if b >= 0 && !checked[b] && bfs(arr, checked, b) {
    return true
  } else if f < len(arr) && bfs(arr, checked, f) {
    return true
  } else {
    return false
  }
}
func canReach(arr []int, start int) bool {
  // BFS
  checked := make(bool[], len(arr))
  return bfs(arr, checked, start)
}
