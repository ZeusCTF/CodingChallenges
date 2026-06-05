// Q2: What does the call to len1() produce?
//
// In main():
//   char s[10] = "foo"
//   sizeof(s)  = 10   (the full array size as declared)
//   strlen(s)  = 3    (characters before the null terminator)
//   Output: "size: 10, len: 3"
//
// In len1(char s[]):
//   When an array is passed to a function, it DECAYS to a pointer.
//   The parameter `char s[]` is identical to `char *s`.
//   sizeof(s) is therefore sizeof(char *) = 8 on a 64-bit system, NOT 10.
//   strlen(s) still = 3 because the data hasn't changed.
//   Output: "size: 8, len: 3"
//
// Key takeaway: sizeof on a function parameter that was declared as an array
// gives the pointer size, not the original array size.  Always pass the
// array length separately when a function needs it.
#include <stdio.h>
#include <string.h>

void len1(char s[]) {
    printf("len1 → size: %zu, len: %zu\n", sizeof(s), strlen(s));
    /* size: 8 (pointer), len: 3 */
}

int main(void) {
    char s[10] = "foo";
    printf("main → size: %zu, len: %zu\n", sizeof(s), strlen(s));
    /* size: 10, len: 3 */
    len1(s);
    return 0;
}
