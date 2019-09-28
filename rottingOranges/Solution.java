class Solution {
  public int orangesRotting(int[][] grid) {
    boolean done = false;
    boolean noFresh = true;
    boolean noRotten = true;
    boolean noChange;
    int steps = 0;
    while (!done) {
      done = true;
      noChange = true;
      for (int i = 0; i < grid.length; i++)
        for (int j = 0; j < grid[0].length; j++)
          if (grid[i][j] >= 2) noRotten = false;
          else if (grid[i][j] == 0) continue;
          else {
            noFresh = false;
            if (
                (i < grid.length-1 && grid[i+1][j] == steps+2) ||
                (j < grid[0].length-1 && grid[i][j+1] == steps+2) ||
                (i > 0 && grid[i-1][j] == steps+2) ||
                (j > 0 && grid[i][j-1] == steps+2)
               ) {grid[i][j] = steps+3; noChange = false;}
            else if (
                (i == grid.length-1 || grid[i+1][j] == 0) &&
                (j == grid[0].length-1 || grid[i][j+1] == 0) &&
                (i == 0 || grid[i-1][j] == 0) &&
                (j == 0 || grid[i][j-1] == 0)
                ) return -1;
            else done = false;
          }
      steps++;
      if (!done && noChange) return -1;
    }
    return (noFresh)?0:steps;
  }
}
