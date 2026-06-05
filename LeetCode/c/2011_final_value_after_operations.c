/**
 * 2011. Final Value of Variable After Performing Operations
 * https://leetcode.com/problems/final-value-of-variable-after-operations/
 * Difficulty: Easy  Topic: Simulation
 *
 * X starts at 0.  "X++" and "++X" increment; "--X" and "X--" decrement.
 * Return the final value.
 */
#include <string.h>

int finalValueAfterOperations(char **operations, int operationsSize) {
    int res = 0;
    for (int i = 0; i < operationsSize; i++) {
        if (strcmp(operations[i], "X++") == 0 ||
            strcmp(operations[i], "++X") == 0)
            res++;
        else
            res--;
    }
    return res;
}
