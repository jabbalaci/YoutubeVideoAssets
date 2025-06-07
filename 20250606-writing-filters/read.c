#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 512

int main()
{
    char line[BUFFER_SIZE];
    FILE *fp = fopen("szoveg.txt", "r");

    if (fp == NULL)
    {
        fprintf(stderr, "I/O error.\n");
        exit(1);
    }

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        printf("%s", line);
    }

    fclose(fp);

    return 0;
}
