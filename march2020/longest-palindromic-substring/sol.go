package main

import (
  "strings"
  "fmt"
)

func longestPalindrome(s string) string {
  // Naive solution.
  var rsb strings.Builder
  for i := 0; i < len(s); i++ {
    rsb.WriteByte(s[len(s) - i - 1])
  }
  rs := rsb.String()
  if rs == s {
    return s
  } else {
    ls := longestPalindrome(string(s[:len(s)-1]))
    rs := longestPalindrome(string(s[1:]))
    if len(ls) >= len(rs) {
      return ls
    } else {
      return rs
    }
  }
}

func main() {
  fmt.Print(longestPalindrome("raceca"))
}
