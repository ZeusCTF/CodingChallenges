// Q2: What does the following program output?
//
// Three sequential fork() calls create a binary tree of processes.
// Label the original process P0.  After each fork, both parent and child
// continue executing from that point.
//
// Process tree and the value of x each process holds when it reaches printf:
//
//  fork #1 (x starts at 0)
//    P0  → x stays 0          (parent of fork #1)
//    P1  → x = 0 + 4 = 4      (child  of fork #1)
//
//  fork #2 (both P0 and P1 reach this)
//    P0  → x stays 0          (parent of fork #2)
//    P2  → x = 0 + 2 = 2      (child  of fork #2, inherits x=0 from P0)
//    P1  → x stays 4          (parent of fork #2)
//    P3  → x = 4 + 2 = 6      (child  of fork #2, inherits x=4 from P1)
//
//  fork #3 (all four processes reach this)
//    P0  → x stays 0          (parent of fork #3)
//    P4  → x = 0 + 1 = 1      (child  of fork #3, inherits x=0)
//    P2  → x stays 2
//    P5  → x = 2 + 1 = 3      (child  of fork #3, inherits x=2)
//    P1  → x stays 4
//    P6  → x = 4 + 1 = 5      (child  of fork #3, inherits x=4)
//    P3  → x stays 6
//    P7  → x = 6 + 1 = 7      (child  of fork #3, inherits x=6)
//
// 8 processes print (in some interleaved order): 0 1 2 3 4 5 6 7
// Sum = 28  (not 12 or 14 — earlier comments in this file were incorrect)
//
// The original note said "expected 14, got 12."  Both are wrong.
// The actual printed values are the eight numbers above; the scheduler
// determines their order.
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(void) {
    pid_t childpid;
    int x = 0;

    childpid = fork();
    if (childpid == 0)
        x = x + 4;

    childpid = fork();
    if (childpid == 0)
        x = x + 2;

    childpid = fork();
    if (childpid == 0)
        x = x + 1;

    printf("%d\n", x);
    return 0;
}
