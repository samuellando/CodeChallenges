func isHappy(n int) bool {
  if n <= 0 {
    return false
  }
  seen := make([]bool, 103)
  seen[n] = true
  for n != 1 {
    sum := 0
    for n != 0 {
      sum += (n % 10) * (n % 10)
      n /= 10
    }
    if seen[sum % 103] {
      return false
    }
    seen[sum % 103] = true
    n = sum
  }
  return true
}

