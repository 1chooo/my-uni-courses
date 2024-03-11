#include "stdio.h"
#include "stdlib.h"

#define MAX_STACK_SIZE 1000

int stack[MAX_STACK_SIZE];

int main(void) {
  int N;
  int M;
  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    scanf("%d", &M);

    for (int j = 1; j <= M; j++) {
      scanf("%d", &stack[i]);
      printf("%d ", stack[i]);
    }
    printf("\n");

    for (int j = 1; j <= M; j++) {
      printf("%d ", stack[i]);
    }
    printf("\n");

  }
  
	return 0;
}