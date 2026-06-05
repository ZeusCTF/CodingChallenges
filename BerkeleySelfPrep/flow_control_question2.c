// Q2: What output does the following code produce?
//
// Trace:
//   i = 3, x = 0, y = 0
//
//   while (i >= 0): runs for i = 3, 2, 1, 0  → x increments 4 times → x = 4
//   After loop: i = -1
//
//   do-while (i <= 3): runs for i = -1, 0, 1, 2, 3 → y increments 5 times → y = 5
//   After loop: i = 4
//
//   printf(x - y) → 4 - 5 = -1
//
// Output: -1
#include <stdio.h>

int main(void) {
    int x, y;
    int i = 3;
    x = y = 0;

    while (i >= 0) {
        x += 1;
        i--;
    }
    // x = 4, i = -1

    do {
        y += 1;
        i++;
    } while (i <= 3);
    // y = 5, i = 4

    printf("%d\n", (x - y));  /* prints -1 */
    return 0;
}
