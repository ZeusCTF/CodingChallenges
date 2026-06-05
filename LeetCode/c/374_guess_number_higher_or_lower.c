/**
 * 374. Guess Number Higher or Lower
 * https://leetcode.com/problems/guess-number-higher-or-lower/
 * Difficulty: Easy  Topic: Binary Search
 *
 * A number 1..n is picked.  guess(num) returns:
 *   -1 if num is too high, 1 if too low, 0 if correct.
 * Find the number using binary search.
 */
#include <math.h>

int guess(int num);  /* provided by the judge */

int guessNumber(int n) {
    int lower = 1;
    int upper = n;
    while (lower <= upper) {
        int mid = lower + (upper - lower) / 2;  /* avoids overflow */
        int res = guess(mid);
        if      (res ==  0) return mid;
        else if (res ==  1) lower = mid + 1;
        else                upper = mid - 1;
    }
    return -1;
}
