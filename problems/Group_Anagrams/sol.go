package main

import (
  "fmt"
)

func groupAnagrams(strs []string) [][]string {
  groups := make([][]string, 0)
  sigs := make([][]int, 0)
  for i := 0; i < len(strs); i++ {
    sig := make([]int, 26)
    for j := 0; j < len(strs[i]); j++ {
      sig[strs[i][j] - 97] += 1
    }
    var match bool
    for j := 0; j < len(sigs); j++ {
      match = true
      for k := 0; k < 26; k++ {
        if sigs[j][k] != sig[k] {
          match = false
          break
        }
      }
      if match {
        groups[j] = append(groups[j], strs[i])
        break
      }
    }
    if !match {
      group := make([]string, 1)
      group[0] = strs[i]
      groups = append(groups, group)
      sigs = append(sigs, sig)
    }
  }
  return groups
}

func main() {
  fmt.Println(groupAnagrams([]string{}))
}
