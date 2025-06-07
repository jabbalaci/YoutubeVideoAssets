#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 512

int main()
{
    char line[BUFFER_SIZE];

    printf("Name: ");

    fgets(line, sizeof(line), stdin);
    line[strlen(line) - 1] = '\0';

    printf("Hello %s!\n", line);

    return 0;
}
