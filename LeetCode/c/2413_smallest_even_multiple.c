/**
 * 2413. Smallest Even Multiple
 * https://leetcode.com/problems/smallest-even-multiple/
 * Difficulty: Easy  Topic: Math
 *
 * Return the smallest positive integer that is a multiple of both 2 and n.
 * If n is even it is already a multiple of 2; otherwise 2*n is.
 */
int smallestEvenMultiple(int n) {
    return (n % 2 == 0) ? n : n * 2;
}
