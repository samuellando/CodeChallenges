package main

import (
  "fmt"
)

func uniquePathsIII(grid [][]int) int {
  /*
   * We can use BFS to solve this problem. For the fun of it, let's use
   * golangs concurency features.
   */

  // Find the starting point.
  starti := 0
  startj := 0
  for i := 0; i < len(grid); i++ {
    for j := 0; j < len(grid[i]); j++ {
      if grid[i][j] == 1 {
        starti = i
        startj = j
      }
    }
  }

  // Create the initial instances for the recursions.
  visited := make([][]int, len(grid))
  for i := range visited {
    visited[i] = make([]int, len(grid[0]))
  }
  c := make(chan int)

  // Begin the concurent recusion search.
  go bfs(grid, visited, starti, startj, c)

  // Wait for the response.
  return <-c
}

func bfs(grid, visited [][]int, i, j int, c chan int) {
  // Base cases
  if len(grid) == 0 {
    c <- 0
    return 0
  }
  if grid[i][j] == -1 {
    c <- 0
    return
  }
  // If this is the final position.
  if grid[i][j] == 2 {
    // Check that the taken path was hamiltonian.
    for k := 0; k < len(visitedc); k++ {
      for l := 0; l < len(visitedc[0]); l++ {
        if i != k && j != l && visitedc[k][l] == 0 && grid[k][l] != -1 {
          c <- 0
          return
        }
      }
    }
    c <- 1
    return
  }

  // Create the visited array for the next recursions.
  visitedc := make([][]int, len(grid))
  for i := range visitedc {
    visitedc[i] = make([]int, len(grid[0]))
    copy(visitedc[i], visited[i])
  }
  visitedc[i][j] = 1

  // Create a new channel to recive the counts form reach recursion.
  cc := make(chan int)
  dispatch := 0

  if i > 0 && visited[i-1][j] == 0 {
    go backtrack(grid, visitedc, i-1, j, cc)
    dispatch++
  }
  if i < len(grid)-1 && visited[i+1][j] == 0 {
    go backtrack(grid, visitedc, i+1, j, cc)
    dispatch++
  }
  if j > 0 && visited[i][j-1] == 0 {
    go backtrack(grid, visitedc, i, j-1, cc)
    dispatch++
  }
  if j < len(grid[0])-1 && visited[i][j+1] == 0 {
    go backtrack(grid, visitedc, i, j+1, cc)
    dispatch++
  }

  // Recive a message from each recursion.
  sum := 0
  for i := 0; i < dispatch; i++ {
    sum += <-cc
  }

  // Send the count back to parent.
  c <- sum
  return
}

func main() {
  i := make([][]int, 3)
  i[0] = []int{1,0,0,0}
  i[1] = []int{0,0,0,0}
  i[2] = []int{0,0,2,-1}
  fmt.Println(uniquePathsIII(i))
}
