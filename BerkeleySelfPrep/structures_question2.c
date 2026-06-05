// Q2: What does the following code print?
//
// The anonymous struct has:
//   char s[3]   → 3 bytes
//   int  i      → 4 bytes (typically)
//
// Due to alignment, the compiler inserts 1 byte of padding after s[] so
// that i begins on a 4-byte boundary.  Total sizeof(x) = 8.
//
// Expression 1: (char *)&x.i - x.s
//   &x.i is the address of the int member.
//   Cast to char* and subtract x.s (the address of s[0]).
//   This is the byte offset of i within the struct = 4 (3 bytes of s + 1 pad).
//   Output: 4
//
// Expression 2: sizeof(x) - sizeof(x.s) - sizeof(x.i)
//   8 - 3 - 4 = 1  (the 1 byte of padding)
//   Output: 1
#include <stdio.h>

int main(void) {
    struct {
        char s[3];
        int  i;
    } x;

    printf("%d\n", (int)((char *)&x.i - x.s));        /* 4 */
    printf("%d\n", (int)(sizeof(x) - sizeof(x.s) - sizeof(x.i))); /* 1 */
    return 0;
}
