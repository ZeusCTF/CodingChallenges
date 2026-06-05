// Q1: What does the following program do?
//
// This program counts the number of newline characters in the file passed as
// argv[1], then prints that count.  It is equivalent to `wc -l <file>`.
#include <stdio.h>

int main(int argc, char **argv) {
    FILE *fp;
    int x = 0;
    int c;

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    fp = fopen(argv[1], "r");
    if (!fp) {
        perror("fopen");
        return 1;
    }

    for (c = getc(fp); c != EOF; c = getc(fp)) {
        if (c == '\n')
            x++;
    }

    fclose(fp);
    printf("%d\n", x);
    return 0;
}
