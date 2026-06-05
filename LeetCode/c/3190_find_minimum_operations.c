/**
 * 3190. Find Minimum Operations to Make All Array Elements Divisible by Three
 * https://leetcode.com/problems/find-minimum-operations-to-make-all-array-elements-divisible-by-three/
 * Difficulty: Easy  Topic: Array, Math
 *
 * For each element not divisible by 3, one operation (±1) makes it so.
 * Return the count of such elements.
 */
int minimumOperations(int *nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize; i++)
        if (nums[i] % 3 != 0) res++;
    return res;
}
