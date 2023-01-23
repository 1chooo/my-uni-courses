#include "stdio.h"
#include "stdlib.h"

/*
1. CreateStack with struct
2. IsEmpty(), Isfull to check whether we can store more.
3. Create the mechanics: Add, Delete.
*/

#define MAX_STACK_SIZE 100

typedef struct element {
  int key;
} Element;

Element stack[MAX_STACK_SIZE];
int top = -1;

bool stack_empty(stack) ::= top < 0;
bool stack_full(stack) ::= top >= MAX_STACK_SIZE;

void add(int *top, Element item) {
  if (*top >= MAX_STACK_SIZE) {
    stack_full();

    return;
  }
  stack[++*top] = item;
}

Element delete(int *top) {
  if (*top == -1)
    return stack_empty();

  return stack[(*top)--];
}