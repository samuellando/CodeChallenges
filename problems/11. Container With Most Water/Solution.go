func min(x, y int) int {
    if x > y {
        return y
    } else {
        return x
    }
}

func max(x, y int) int {
    if x > y {
        return x
    } else {
        return y
    }
}

func abs(x int) int {
    if x > 0 {
        return x
    } else {
        return -1 * x
    }
}

// O(n^2) solution. 

func maxArea1(height []int) int {
  var global_max, my_max, a int = 0, 0, 0
  global_max = 0
  for i := 0; i < len(height); i++ {
    my_max = 0
    for j := 0; j < len(height); j++ {
      a = int(min(height[i], height[j]) * (abs(i - j)))
      if a > my_max {
        my_max = a
      }
    }
    if my_max > global_max {
      global_max = my_max
    }
  }
    
  return global_max
}

// O(n) start with the widest, and move in

func maxArea(height []int) int {
  var mx, l, r int = 0, 0, len(height) - 1

  for l < r {
    mx = max(mx, min(height[l], height[r])*(r - l))

    if height[l] > height[r] {
      r--
    } else {
      l++
    }
  }

  return mx
}
