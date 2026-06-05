// Q1: What numbers are printed by the following loops?
#include <stdio.h>

int main(void) {
    // Loop 1: i starts at 0, runs while i < 5, increments after the check.
    // Prints: 0, 1, 2, 3, 4
    for (int i = 0; i < 5; ++i)
        printf("loop 1: %d\n", i);

    // Loop 2: i starts at 1, runs while i <= 5.
    // Prints: 1, 2, 3, 4, 5
    for (int i = 1; i <= 5; ++i)
        printf("loop 2: %d\n", i);

    // Loop 3: i starts at 5, counts down while i > 0.
    // Prints: 5, 4, 3, 2, 1
    for (int i = 5; i > 0; --i)
        printf("loop 3: %d\n", i);

    // Loop 4: no initializer; condition is --i (pre-decrement), which
    // evaluates to the new value of i.  Loop exits when --i reaches 0
    // (falsy), so the body never runs when i would be 0.
    // Starting from i=5: prints 4, 3, 2, 1  (stops before printing 0)
    for (int i = 5; --i;)
        printf("loop 4: %d\n", i);

    return 0;
}
