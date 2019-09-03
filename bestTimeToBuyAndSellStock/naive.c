// n^2.
int maxProfit(int* prices, int pricesSize){
  // Generate array that will store the maximum profit if you buy at price i.
  int maxProfit[pricesSize];
  // Fill maxProfit.
  int max;
  for (int i = 0; i < pricesSize; i++) {
    max = 0;
    for (int j = i+1; j < pricesSize; j++)
      if ((*(prices + j) - *(prices + i)) > max)
        max = (*(prices + j) - *(prices + i));
    maxProfit[i] = max;
  } 
  // Determine the highest mex profit.
  max = maxProfit[0];
  for (int i = 1; i < pricesSize; i++)
    if (maxProfit[i] > max)
      max = maxProfit[i];
  return max;
}
