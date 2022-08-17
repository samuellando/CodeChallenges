func countBits(n int) []int {
  a := make([]int, n+1)
  j := 0
  for i := 0; i < len(a); i++ {
    j = i
    for j > 0 {
      if j & 1 == 1 {
        a[i]++
      }
      j = j >> 1

    }
  }

  return a
}
