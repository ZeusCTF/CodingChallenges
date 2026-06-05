// Q2: Explain what the program below does.
//
// 1. setenv("PATH", "/some/path/bin", 1) sets the PATH environment variable
//    to "/some/path/bin".  The third argument (1) means overwrite if PATH
//    already exists.
//
// 2. The program then iterates over `environ` (the global array of
//    "KEY=value" strings that represents the process's entire environment)
//    and prints each entry with puts().
//
// Effect: replaces PATH in the current process's environment, then dumps
// all environment variables to stdout.
//
// Note: changes to the environment via setenv() affect only the current
// process and any child processes it spawns afterward; the parent shell's
// environment is not modified.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

int main(void) {
    if (setenv("PATH", "/some/path/bin", 1) != 0) {
        perror("setenv");
        return 1;
    }

    if (environ != NULL) {
        for (size_t i = 0; environ[i] != NULL; ++i)
            puts(environ[i]);
    }

    return 0;
}
