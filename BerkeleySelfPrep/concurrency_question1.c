// Q1: Assuming printString prints the string one character at a time,
//     what is the output of the following program?
//
// After fork(), two processes run concurrently:
//   Parent (pid > 0): calls printString("Hello\n")
//   Child  (pid == 0): calls printString("World!\n")
//
// Because both processes write one character at a time and the OS scheduler
// can interleave them at any point, the output is NON-DETERMINISTIC.
// A possible output:
//
//   H
//   W
//   e
//   o
//   l
//   r
//   l
//   l
//   o
//   d
//   (newline)
//   !
//   (newline)
//
// The only guarantee is that all characters of each string eventually appear;
// their relative ordering depends on the scheduler.
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/* Provided externally in the original exercise */
void printString(const char *s);

int main(void) {
    pid_t pid = fork();
    if (pid > 0) {
        printString("Hello\n");
    } else {
        printString("World!\n");
    }
    return 0;
}
