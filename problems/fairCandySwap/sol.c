#include <stdlib.h>
/*
 * Note: The returned array must be malloced, assume caller calls free().
 * In this solution we use a basic hash.
 */
int* fairCandySwap(int* A, int ASize, int* B, int BSize, int* returnSize){
  *returnSize = 2;
  int *ans = (int *) malloc((*returnSize) * sizeof(int));
  int *tableA = (int *) calloc(100001, sizeof(int));
  int *tableB = (int *) calloc(100001, sizeof(int));
  // Determine the difference of the summs and hash elements.
  int diff = 0;
  for (int i = 0; i < ASize; i++) {
    *(tableA + (*(A + i))) = 1;
    diff += *(A + i);
  }
  for (int i = 0; i < BSize; i++) {
    *(tableB + (*(B + i))) = 1;
    diff -= *(B + i);
  }
  diff /= 2;
  int bMina = 0;
  if (diff < 0) {
    bMina = 1;
    diff *= -1;
  }
  // Iterate throught possible solutions and return the first valid one.
  for (*(ans + (bMina?0:1)) = 1; true; (*(ans + (bMina?0:1)))++) {
    *(ans + (bMina?1:0)) = (*(ans + (bMina?0:1))) + diff;
    if (*(tableA + (*(ans))) && *(tableB + (*(ans + 1))))
      return ans;
  }
  return ans;
}
