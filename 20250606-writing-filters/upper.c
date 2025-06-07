#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 512

int main()
{
    char line[BUFFER_SIZE];

    while (fgets(line, sizeof(line), stdin) != NULL)
    {
        for (int i = 0; line[i] != '\0'; ++i)
        {
            line[i] = toupper(line[i]);
        }
        printf("%s", line);
    }

    return 0;
}
