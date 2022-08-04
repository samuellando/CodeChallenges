package main


import (
  "fmt"
)

func backspaceCompare(S string, T string) bool {
  // The simple way if to determine the resulting strings and then compare them.
  s1 := make([]byte, 200)
  s2 := make([]byte, 200)

  fast := 0
  slow := 0
  for fast < len(S) {
    if S[fast] == '#' {
      if slow > 0 {
        slow--
        s1[slow] = 0
      }
    } else {
      s1[slow] = S[fast]
      slow++
    }
    fast++
  }

  fast = 0
  slow = 0
  for fast < len(T) {
    if T[fast] == '#' {
      if slow > 0 {
        slow--
        s2[slow] = 0
      }
    } else {
      s2[slow] = T[fast]
      slow++
    }
    fast++
  }

  for i := 0; i < 200; i++ {
    if s1[i] != s2[i] {
      return false
    }
  }
  return true
}

func main() {
  fmt.Println(backspaceCompare("##", ""))
}
