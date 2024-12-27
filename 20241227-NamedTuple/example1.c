#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

int main()
{
    Point p = {2, 1};

    // Point p = {
    // .y = 1,
    // .x = 2
    // };

    // Point p = {y: 1, x: 2};

    printf("Point(x=%d, y=%d)\n", p.x, p.y);

    return 0;
}
