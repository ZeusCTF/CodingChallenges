// Q3: What do the following functions do?
//
// counti(int n):
//   Decrements n and prints it as a signed integer while n-- >= 0.
//   For n=3 it prints: 2, 1, 0, then -1 (the post-decrement makes the
//   condition check the old value; the body receives the already-decremented
//   value).  Terminates normally once n is negative.
//
// countu(unsigned n):
//   Appears identical but n is unsigned.  Unsigned integers cannot be
//   negative: when n reaches 0, n-- in the condition evaluates to 0
//   (falsy for the check) BUT simultaneously wraps n around to UINT_MAX
//   (a very large positive number like 4294967295).  The condition then
//   sees UINT_MAX >= 0, which is always true for an unsigned value, so the
//   loop continues.  THIS IS AN INFINITE LOOP printing a countdown from
//   UINT_MAX.
//
// Key takeaway: never use unsigned types as loop counters when the
// termination condition relies on reaching a negative value.
#include <stdio.h>

void countu(unsigned n) {
    while (n-- >= 0)          /* always true for unsigned → infinite loop */
        printf("%u\n", n);
}

void counti(int n) {
    while (n-- >= 0)          /* terminates once n goes negative */
        printf("%d\n", n);
}
