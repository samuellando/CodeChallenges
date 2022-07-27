// O(n), too slow.
func divide(dividend int, divisor int) int {
    positive := true

  if dividend < 0 && divisor < 0 {
    positive = true
  } else if dividend < 0 || divisor < 0 {
    positive = false
  }

  up := false
  if dividend < 0 {
    up = true  
  }
  var i int = 0
  for (dividend > 0 && !up) || (dividend < 0 && up) {
    if positive {
      dividend -= divisor
      i++
    } else {
      dividend += divisor
      i--
    }
  }
  
  if dividend != 0 {
    if i > 0 {
      i--
    } else {
      i++
    }
  }
    
  if i > 2147483647 {
    return 2147483647
  } 
  if i < -2147483648 {
    return -2147483648 
  }
    
  return i
}
