#include "stdlib.h"
#include "stdio.h"

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

// typedef struct listNode *listPointer;

// typedef struct listNode {
//   char data[4];
//   listPointer link;
// } ListNode;

// listPointer ptr = NULL;

#define MAX_STACKS 10

typedef struct element{
  int key;
} Element;

typedef struct stack *stackPointer;

typedef struct stack {
  Element item;
  stackPointer link;
} Stack;

stackPointer top[MAX_STACKS];


void add(stackPointer *top, Element item) {
  stackPointer temp = (stackPointer) malloc(sizeof(stack));

  if (IS_FULL(temp)) {
    fprintf(stderr, "The memory is full\n");
    exit(1);
  }

  temp -> item = item;
  temp -> link = *top;
  *top = temp;

  return;
}


Element delete(stackPoiter *top) {
  stackPointer temp = *top;
  Element item;

  if (IS_EMPTY(temp)) {
    fprintf(stderr, "The stack is empty\n");
    exit(1);
  }

  item = item -> item;
  *top = temp -> link;

  free(temp);

  return item;
}