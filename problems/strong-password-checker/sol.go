// UNSOLVED!
package main

import (
  "fmt"
)

func strongPasswordChecker(s string) int {
  /* 
    Lets begin by finding all the repeat blocks and checking that each type 
    exists in the string.

    O(n)
   */
   repeats := make(int, 0)
   hasLowerCase := 0
   hasUpperCase := 0
   hasDigit := 0
   for i := 0; i <= len(s); i++ {
     if s[i] >= 'a' && s[i] <= 'z' {
       hasLowerCase = 1
     }
     if s[i] >= 'A' && s[i] <= 'Z' {
       hasUpperCase = 1
     }
     if s[i] >= '1' && s[i] <= '9' {
       hasDigit = 1
     }
     repLen := 1
     for s[i] == s[i+1]; i++ {
       repLen++
     }
     if repLen >= 3 {
       repeats = append(repeats, repLen)
     }
   }
   missingTypes := hasLowerCase + hasUpperCase + hasDigit

   /*
      Cases:
        - len(s) < 6: insert until length is 6, prioritze missing types, insert
          remaining missing types. There can be at most on repeat block, either
          case is solved.

        - len(s) > 20: no insertions. Repeats can be solved by repacement
          or shirnking the block to a size of 2.

        - 6 <= len(s) <= 20: only do replacements. Replace by missing types first.
    */

    ins := 0
    del := 0
    rep := 0
    if len(s) < 6 {
      ins = 6 - len(s)
      if ins < missingTypes {
        rep = missingTypes - ins
      }
    }

    if len(s) > 20 {
      allDel := 0
      for i := 0; i < len(repeats); i++ {
        allDel = repeats[i] - 2
      }

      del := len(s) - 20

      if del < allDel {
        // This means we can solve some repeats by replacement instead.
        repDel := (repDel - del)
      }
      return changes
    }
}

func main() {
  fmt.Println(strongPasswordChecker("aaabbbcccdddeeefffA1"))
}
