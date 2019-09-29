class Solution {
  public int[][] generateMatrix(int n) {
    int[][] m = new int[n][n];
    int k = 0;
    int i = 0;
    int j = 0;
    int stage = 0; // 0,1,2,3
    int l = 0;
    int d = n;
    while (k < n*n) {
      System.out.println("("+i+","+j+")");
      m[j][i] = ++k;
      if (stage == 0)
        if (++l < d) i++;
        else {stage = 1; l = 1; j++;}
      else if (stage == 1)
        if (++l < d) j++;
        else {stage = 2; l = 1; i--;}
      else if (stage == 2)
        if (++l < d) i--;
        else {stage = 3; l = 1; d--; j--;}
      else
        if (++l < d) j--;
        else {stage = 0; l = 0; i++; d--;}
    }
    return m; 
  }
}
