// Q2: Explain the behavior of the three code fragments.
//
// In each case the input is: "line one\nline two\n"
//
// --- fgets ---
// fgets(s1, 10, stdin) reads at most 9 characters plus a null terminator.
// It stops at a newline (keeping it) or EOF.
// Input "line one\n" → s1 = "line one\n" (9 chars + '\0') → strlen = 9.
//
// --- scanf %s ---
// scanf("%9s", s2) reads a whitespace-delimited token of at most 9 chars.
// It stops at the first space, so it reads "line" → strlen = 4.
// Note: %s skips leading whitespace and never includes it in the result.
//
// --- scanf %c ---
// scanf("%10c", s3) reads exactly 10 raw characters with no null terminator.
// s3 is NOT a valid C string after this call; strlen behavior is undefined
// because there is no '\0'.  On most systems it will read "line one\n " and
// return some garbage length depending on whatever follows s3 in memory.
//
// Summary:
//   fgets   → safest; null-terminates; preserves newline
//   %s      → stops at whitespace; null-terminates; skips leading whitespace
//   %c      → reads raw bytes; does NOT null-terminate → strlen is undefined
#include <stdio.h>
#include <string.h>

int main(void) {
    char s1[10];
    fgets(s1, 10, stdin);
    printf("fgets  strlen: %zu\n", strlen(s1));   /* typically 9 */

    char s2[10];
    scanf("%9s", s2);
    printf("%%s     strlen: %zu\n", strlen(s2));  /* typically 4 ("line") */

    /* s3 intentionally omitted: %10c does not null-terminate the buffer,
     * making strlen(s3) undefined behavior.  Shown here for illustration only. */
    return 0;
}
