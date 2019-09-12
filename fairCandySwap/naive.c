#include <stdlib.h>
#include <stddef.h>
/*
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fairCandySwap(int* A, int ASize, int* B, int BSize, int* returnSize){
  *returnSize = 2;
  int *ans = (int *) malloc((*returnSize) * sizeof(int));
  // First determine the difference fo the sum from A to B.
  int diff = 0;
  for (int i = 0; i < ASize; i++)
    diff += *(A + i);
  for (int i = 0; i < BSize; i++)
    diff -= *(B + i);
  // The difference of the swaped items is half of this.
  diff /= 2;
  // Find the first possible solution O(sizeA * sizeB).
  for (int i = 0; i < ASize; i++)
    for (int j = 0; j < BSize; j++)
      if (diff == *(A + i) - *(B + j)) {
        *(ans) = *(A + i);
        *(ans + 1) = *(B + j);
        return ans;
      }
  return ans;
}
