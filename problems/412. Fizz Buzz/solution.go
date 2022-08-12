func fizzBuzz(n int) []string {
  arr := make([]string, n)
  for i := 1; i <= n; i++ {
    s := ""
    if i %3 == 0 {
      s += "Fizz"
    }
    if i % 5 == 0 {
      s += "Buzz"
    }
    if s == "" {
      s = fmt.Sprintf("%d", i)
    }
    arr[i-1] = s
  }

  return arr
}
