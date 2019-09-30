#include <stdlib.h>
#include <limits.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
  *(returnSize) = 2;
  int maxNum = INT_MAX;
  int* sol = malloc(sizeof(int) * *(returnSize));
  *(sol) = 4;
  int* hash = calloc(sizeof(int), maxNum*2);
  for (int i = 0; i < numsSize; i++) {
    if (hash[target - *(nums + i) + maxNum] ) {
      *(sol) = hash[target - *(nums + i) + maxNum] - 1;
      *(sol + 1) = i;
      return sol;
    } else
      hash[*(nums + i) + maxNum] = i + 1;
  }
  // To make the compiler happy.
  return sol;
}
