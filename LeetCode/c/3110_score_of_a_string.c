/**
 * 3110. Score of a String
 * https://leetcode.com/problems/score-of-a-string/
 * Difficulty: Easy  Topic: String
 *
 * Return the sum of absolute differences of ASCII values between adjacent
 * characters.
 */
#include <string.h>
#include <stdlib.h>

int scoreOfString(char *s) {
    int res = 0;
    for (size_t i = 0; i + 1 < strlen(s); i++)
        res += abs(s[i] - s[i + 1]);
    return res;
}
