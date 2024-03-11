#include "stdlib.h"
#include "stdio.h"
#include "math.h"

#define MAX_SIZE 101
// #define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))
#define SWAP(x, y, t) (t = x, x = y, y = t)

void sort(int [], int); /* Selection sort */

int main(void) {
    int i, n;
    int list[MAX_SIZE];

    printf("Enter the number of numbers to generate: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {   /* randomly generate numbers. */
        list[i] = rand() % 1000;
        printf("%d ", list[i]);
    }
    sort(list, n);

    printf("\n Sorted array:\n ");

    for (int i = 0; i < n; i++) {   /* print out sorted numbers. */
        printf("%d ", list[i]);
    }
    printf("\n");

    return 0;
}

void sort(int list[], int n) {
    int i, j, min, temp;

    for (i = 0; i < n - 1; i++) {
        min = j;

        for (j = i + 1; j < n; j++) {
            if (list[j] < list[min]) {
                min = j;
            }
        }

        SWAP(list[i], list[min], temp);
    }
    return;
}
