#include "stdio.h"
#include "stdlib.h"
#include "time.h"

#define MAX_SIZE 1601
#define ITERATIONS 26
#define SWAP(x, y, t) = (t = x, x = y, y = t)

int main(void) {
  int i, j, position;
  int list[MAX_SIZE];
  int sizeList[] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 
                    100, 200, 300, 400, 500, 600, 700, 800, 900, 
                    1000, 1100, 1200, 1300, 1400, 1500, 1600};
  clock_t start, stop;
  double duration;

  printf("   n   times\n");

  for (i = 0; i < ITERATIONS; i++) {
    for (j = 0; j < sizeList[i]; j++) {
      list[j] = sizeList[i] - j;
    }

    start = clock();
    sort(list, sizeList[i]);
    stop = clock();

    duration = ((double) (stop - start)) / CLOCKS_PER_SEC;  /* Use CLOCKS_PER_SEC insted of CLK_TCK */
    printf("%6d    %f\n", sizeList[i], duration);
  }

  return 0;
}