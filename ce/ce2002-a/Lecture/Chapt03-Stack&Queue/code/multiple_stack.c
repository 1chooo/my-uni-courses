#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MEMORY_SIZE 100
#define MAX_STACKS 10

typedef struct element {
  int key;
} Element;

/* Global memory declaration */
Element memory[MEMORY_SIZE];
Element delete(int);
int top[MAX_STACKS];
int boundary[MAX_STACKS];
void add(int, Element), stack_full(), stack_empty();

int main(void) {
  int n;
  top[0] = boundary[0] = -1;

  for (int i = 1; i < n; i++)
    top[i] = boundary[i] = (MEMORY_SIZE / n) * i;
  boundary[n] = MEMORY_SIZE - 1;

  return 0;
}

void add(int i, Element item) {
  if (top[i] == boundary[i + 1])
    stack_full(i);

  memory[++top[i]] = item;

  return;
}

Element delete(int i) {
  if (top[i] == boundary[i])
    return stack_empty();
  
  return memory[top[i]--];
}

void stack_full() {
    fprintf(stderr, "error: stack is full\n");

    return;
}

void stack_empty() {
    fprintf(stderr, "error: stack is empty\n");

    return;
}