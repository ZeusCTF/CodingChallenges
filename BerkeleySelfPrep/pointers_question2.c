// Q2: What does the following program print when run with: ./prog one two three
//
// argv is: {"./prog", "one", "two", "three", NULL}
//
// The outer loop: ++argv skips argv[0] (the program name).
//   Each iteration assigns *argv to p (a pointer to the current argument
//   string) and continues while p is non-null (i.e., not the sentinel NULL).
//
// The inner loop: walks p character by character, printing each via putchar,
//   stopping when *p is '\0'.
//
// No spaces or newlines are added between arguments.
// Output:  onetwothree
#include <stdio.h>

int main(int argc, char *argv[]) {
    for (char *p; (p = *++argv) != NULL;)
        for (; *p; ++p)
            putchar(*p);
    putchar('\n');
    return 0;
}
