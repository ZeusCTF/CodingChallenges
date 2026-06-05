/**
 * 1929. Concatenation of Array
 * https://leetcode.com/problems/concatenation-of-array/
 * Difficulty: Easy  Topic: Array
 *
 * Return ans of length 2*n where ans[i] == nums[i] and ans[i+n] == nums[i].
 *
 * Note: The returned array must be malloc'd; the caller calls free().
 */
#include <stdlib.h>

int *getConcatenation(int *nums, int numsSize, int *returnSize) {
    int *arr = (int *)malloc(2 * numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        arr[i]           = nums[i];
        arr[i + numsSize] = nums[i];
    }
    *returnSize = 2 * numsSize;
    return arr;
}
