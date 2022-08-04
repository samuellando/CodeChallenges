class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] right = new int[grid.length];      
        int[] front = new int[grid.length];      

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (grid[i][j] > front[i])
                    front[i] = grid[i][j];
                if (grid[i][j] > right[j])
                    right[j] = grid[i][j];
            }
        }

        int sum = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (grid[i][j] < front[i] && grid[i][j] < right[j])
                    if (front[i] < right[j])
                        sum += front[i] - grid[i][j];
                    else
                        sum += right[j] - grid[i][j];
            }
        }
    }
}