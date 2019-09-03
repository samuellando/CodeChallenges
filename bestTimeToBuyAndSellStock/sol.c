int maxProfit(int* prices, int pricesSize){
  // This algorithm requires an array size of at least 2.
  if (pricesSize < 2) return 0;
  int sell; // store the best selling price.
  int max;  // store the max profit.

  /* 
   * Since we want to know the highest possible selling price at a certain 
   * point, we will loop trhough the prices backwards.
   */
  max = 0;
  sell = prices[pricesSize - 1];
  for (int i = pricesSize - 2; i >= 0; i--)
    if (prices[i] > sell)
      sell = prices[i];
    else if (sell - prices[i] > max)
      max = sell - prices[i];
  return max;
}
