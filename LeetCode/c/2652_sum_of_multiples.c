/**
 * 2652. Sum of Multiples
 * https://leetcode.com/problems/sum-of-multiples/
 * Difficulty: Easy  Topic: Math
 *
 * Return the sum of all integers in [1, n] that are divisible by 3, 5, or 7.
 */
int sumOfMultiples(int n) {
    int res = 0;
    for (int i = 1; i <= n; i++)
        if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0)
            res += i;
    return res;
}
