#include <stdio.h>

int main()
{
    int a, b, c;

    a = 5;

    // a = (b = 8);

    printf("%d\n", a = b = 12);

    return 0;
}
