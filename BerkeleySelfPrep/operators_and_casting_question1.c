// Q1: Explain the difference between these two expressions.
//
// Version A:  x += (y += z)
//   Evaluation order is right-to-left for the inner assignment:
//     y += z  →  y = 1 + 1 = 2
//     x += y  →  x = 1 + 2 = 3
//   Output: x=3, y=2, z=1  ✓ compiles and runs correctly
//
// Version B:  (x += y) += z
//   The sub-expression (x += y) is an assignment expression.  In C, the
//   result of an assignment is an rvalue (not an lvalue), so applying
//   another += to it attempts to assign to a temporary — which is illegal.
//   gcc rejects this with: "lvalue required as left operand of assignment"
//   This is UNDEFINED BEHAVIOR per the C standard and fails to compile.
//
// If it hypothetically compiled with one possible evaluation:
//   x += y → x = 2 (but this result is not a valid assignment target)
//   Attempting += z would be undefined; some might expect x=3, y=1, z=1
//   but the compiler is not required to produce any particular result.
#include <stdio.h>

int main(void) {
    int x, y, z;
    x = y = z = 1;

    /* Version A — valid */
    x += (y += z);
    printf("Version A: x=%d y=%d z=%d\n", x, y, z);
    /* Output: x=3 y=2 z=1 */

    /* Version B — does not compile; shown here as a comment only
     *
     * x = y = z = 1;
     * (x += y) += z;   // error: lvalue required as left operand of assignment
     */

    return 0;
}
