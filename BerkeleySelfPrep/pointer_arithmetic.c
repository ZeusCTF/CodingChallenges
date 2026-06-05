// Q1: What does the following function do?
//
// foo() is a manual implementation of strcpy.
// It copies each byte from s into d one character at a time via pointer
// arithmetic.  The assignment (*d_tmp++ = *s_tmp++) copies the current
// character, advances both pointers, and the loop continues until the
// null terminator '\0' is copied (which evaluates to false, ending the loop).
// The function returns a pointer to the start of the destination buffer d.
//
// The `restrict` keyword promises the compiler that d and s do not overlap
// in memory, enabling certain optimizations.
// Casting s to `unsigned char *` avoids signed-char implementation issues
// with characters whose values are > 127.
#include <stdio.h>

char *foo(char *restrict d, const char *restrict s) {
    const unsigned char *s_tmp = (const unsigned char *)s;
    unsigned char *d_tmp = (unsigned char *)d;
    while ((*d_tmp++ = *s_tmp++))
        ;
    return d;
}

int main(void) {
    char dest[20];
    foo(dest, "Hello, world!");
    printf("%s\n", dest);
    return 0;
}
