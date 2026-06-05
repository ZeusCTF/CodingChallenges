// Q1: What is the output of the following program?
//
// strtok splits a string by a delimiter, returning successive tokens.
// On the first call pass the string; on subsequent calls pass NULL to
// continue tokenizing the same string.
//
// str = "item1 item2 item3 item4 item5"
// strtok splits on ' ', yielding: "item1", "item2", "item3", "item4", "item5"
//
// Output:  item1,item2,item3,item4,item5,
// (trailing comma because the loop always appends one)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    const char *str = "item1 item2 item3 item4 item5";

    char *tmp = malloc(strlen(str) + 1);
    if (tmp == NULL) {
        perror("malloc");
        return 1;
    }

    strcpy(tmp, str);

    char *t = strtok(tmp, " ");
    while (t != NULL) {
        printf("%s,", t);
        t = strtok(NULL, " ");
    }
    printf("\n");

    free(tmp);
    tmp = NULL;
    return 0;
}
