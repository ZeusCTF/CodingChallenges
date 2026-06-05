// Q1: What is the output of the following program?
//
// sum() receives pointers to both arrays (arrays decay to pointers in C).
// It modifies array1 IN PLACE by adding array2[i] to each element, then
// returns the total.
//
// Trace inside sum():
//   i=0: a1[0] = 1+1 = 2,  sum = 2
//   i=1: a1[1] = 2+2 = 4,  sum = 6
//   i=2: a1[2] = 3+3 = 6,  sum = 12
//   returns 12
//
// Back in main, array1 is now {2, 4, 6} (mutated), array2 is still {1, 2, 3}.
//
// Output:
//   Elements of the array: 2 4 6
//   2 + 1 + 4 + 2 + 6 + 3 = 12
#include <stdio.h>

#define SIZE 3

int sum(int a1[], int a2[]) {
    int total = 0;
    for (int i = 0; i < SIZE; i++) {
        a1[i] += a2[i];
        total += a1[i];
    }
    return total;
}

int main(void) {
    int array1[SIZE] = {1, 2, 3};
    int array2[SIZE] = {1, 2, 3};

    int x = sum(array1, array2);

    printf("Elements of the array: ");
    for (int j = 0; j < SIZE; ++j)
        printf("%d ", array1[j]);
    printf("\n");

    for (int i = 0; i < SIZE; i++) {
        printf("%d + %d", array1[i], array2[i]);
        if (i < SIZE - 1)
            printf(" + ");
    }
    printf(" = %d\n", x);

    return 0;
}
