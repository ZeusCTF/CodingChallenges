// Q2: What output does the following code produce?
//
// Trace:
//   Initial state: i = 3, x = 3
//
//   Iteration 1: --i → i = 2 (truthy); array[2] = --x = 2 (truthy) → print 2
//   Iteration 2: --i → i = 1 (truthy); array[1] = --x = 1 (truthy) → print 1
//   Iteration 3: --i → i = 0 (FALSY) → loop exits immediately; body not reached
//
// Output:
//   2
//   1
//
// Note: x reaches 1 before i reaches 0, so the loop is controlled by i, not x.
#include <stdio.h>

int main(void) {
    int array[3];
    int i = 3, x = 3;

    while (--i && (array[i] = --x))
        printf("%d\n", array[i]);

    return 0;
}
