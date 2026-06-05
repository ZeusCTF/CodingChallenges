// Q1: What is the output of the following code?
//
// ptr is set to the base address of ary.  On each iteration we dereference
// ptr (printing the integer value) and print the address, then advance ptr
// by 1 (which moves it forward by sizeof(int) bytes, typically 4).
//
// Output (addresses are illustrative — actual values vary per run):
//   11 0x7ffd...0
//   22 0x7ffd...4
//   33 0x7ffd...8
//   44 0x7ffd...c
#include <stdio.h>

int main(void) {
    int ary[4] = {11, 22, 33, 44};
    int *ptr = ary;

    for (int i = 0; i < 4; i++) {
        printf("%d %p\n", *ptr, (void *)ptr);
        ptr++;
    }
    return 0;
}
