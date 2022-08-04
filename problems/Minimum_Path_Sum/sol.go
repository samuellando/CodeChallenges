package main

import (
	"fmt"
)

func mn(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func minPathSum(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}

	dp := make([][]int, len(grid))
	for i := 0; i < len(grid); i++ {
		dp[i] = make([]int, len(grid[i]))
	}

	dp[0][0] = grid[0][0]

	for i := 1; i < len(grid[0]); i++ {
		dp[0][i] = dp[0][i-1] + grid[0][i]
	}
	for i := 1; i < len(grid); i++ {
		dp[i][0] = dp[i-1][0] + grid[i][0]
	}

	for i := 1; i < len(grid); i++ {
		for j := 1; j < len(grid[0]); j++ {
			dp[i][j] = mn(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])
		}
	}

	return dp[len(grid)-1][len(grid[0])-1]
}

func main() {
  i := make([][]int, 3)
  i[0] = []int{1,3,1}
  i[1] = []int{1,5,1}
  i[2] = []int{4,2,1}
  fmt.Println(minPathSum(i))
}