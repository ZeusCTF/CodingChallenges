// Q3: What is the result of running the following program?
//
// arr is a char array (mutable) initialized with "abcc".
// str is a char pointer pointing to a string literal (read-only).
//
// *(arr + 3) = 'd':
//   arr is a stack-allocated array, so individual elements can be modified.
//   arr becomes "abcd".  puts(arr) prints: abcd
//
// *(str + 3) = 'd':
//   str points to a string literal stored in read-only memory (.rodata).
//   Attempting to write to it causes a SEGMENTATION FAULT (undefined behavior).
//   The program crashes before puts(str) can execute.
//
// Lesson: char arr[] = "abc" copies the literal onto the stack (writable).
//         char *str  = "abc" stores a pointer to the literal (read-only).
#include <stdio.h>
#include <string.h>

int main(void) {
    char arr[] = "abcc";  /* mutable copy on the stack */
    char *str  = "abcc";  /* pointer into read-only memory */

    *(arr + 3) = 'd';     /* OK: modifying the stack copy */
    puts(arr);            /* prints: abcd */

    *(str + 3) = 'd';     /* UNDEFINED BEHAVIOR: segfault at runtime */
    puts(str);            /* never reached */

    return 0;
}
