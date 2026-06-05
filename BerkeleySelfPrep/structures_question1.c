// Q1: What is the output when running the following program?
//
// d is a Date struct initialized with day=1, month=1, year=2020.
// d2 is a pointer to d.
// The arrow operator (->) dereferences d2 and accesses the named field.
// d2->day is identical to (*d2).day.
//
// Output:  1/1/2020
#include <stdio.h>

struct Date {
    int day;
    int month;
    int year;
};

int main(void) {
    struct Date d = {1, 1, 2020};
    struct Date *d2 = &d;

    printf("%d/%d/%d\n", d2->day, d2->month, d2->year);
    return 0;
}
