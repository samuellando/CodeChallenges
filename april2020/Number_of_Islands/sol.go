func numIslands(grid [][]byte) int {
	visited := make([][]byte, len(grid))
	for i := 0; i < len(visited); i++ {
		visited[i] = make([]byte, len(grid[i]))
	}

	c := 0
	for i := 0; i < len(visited); i++ {
		for j := 0; j < len(visited[0]); i++ {
			if grid[i][j] == 1 && visited[i][j] == 0 {
				c++
				dfs(grid, visited, i, j)
			}
		}
	}

	return c
}
func dfs(grid, visited [][]int, i, j int) {
	// Base cases
	if len(grid) == 0 {
		return
	}

	visited[i][j] = 1
  
	if i > 0 && visited[i-1][j] == 1 {
	  dfs(grid, visited, i-1, j)
	}
	if i < len(grid)-1 && visited[i+1][j] == 1 {
	  dfs(grid, visited, i+1, j)
	}
	if j > 0 && visited[i][j-1] == 1 {
	  dfs(grid, visited, i, j-1)
	}
	if j < len(grid[0])-1 && visited[i][j+1] == 1 {
	  dfs(grid, visitedc, i, j+1)
	}
	return
  }