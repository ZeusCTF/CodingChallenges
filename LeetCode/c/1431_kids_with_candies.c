/**
 * 1431. Kids With the Greatest Number of Candies
 * https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
 * Difficulty: Easy  Topic: Array
 *
 * For each kid, return true if giving them all extraCandies would make them
 * have at least as many candies as the current maximum.
 *
 * Note: The returned array must be malloc'd; the caller calls free().
 */
#include <stdlib.h>
#include <stdbool.h>

bool *kidsWithCandies(int *candies, int candiesSize,
                      int extraCandies, int *returnSize) {
    /* Find current maximum */
    int max = 0;
    for (int i = 0; i < candiesSize; i++)
        if (candies[i] > max) max = candies[i];

    bool *result = (bool *)malloc(candiesSize * sizeof(bool));
    for (int i = 0; i < candiesSize; i++)
        result[i] = (candies[i] + extraCandies >= max);

    *returnSize = candiesSize;
    return result;
}
