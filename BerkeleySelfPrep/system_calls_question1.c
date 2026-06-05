// Q1: Explain what the program below does.
//
// 1. Retrieves the HOME environment variable via getenv().
// 2. Builds the shell command string "ls -l <HOME> | head -n 5" using snprintf
//    into a fixed-size buffer (safely limiting to MAX_BUF_SIZE characters).
// 3. Executes the command via system(), which spawns a shell.
//
// Effect: prints the first 5 entries of a long-format directory listing of
// the user's home directory.
//
// Security note: system() is generally discouraged in production code because
// it passes a string to a shell, making it vulnerable to command injection if
// any part of the command string comes from untrusted input.  Prefer execv()
// family calls with explicit argument arrays when security matters.
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>

#define MAX_BUF_SIZE 256

int main(void) {
    const char *home;
    char command[MAX_BUF_SIZE];

    home = getenv("HOME");
    if (home == NULL) {
        fprintf(stderr, "HOME not set\n");
        return 1;
    }

    int len = snprintf(command, sizeof(command),
                       "ls -l %s | head -n 5", home);
    if (len < 0 || len >= MAX_BUF_SIZE) {
        fprintf(stderr, "Command buffer too small\n");
        return 1;
    }

    system(command);
    return 0;
}
