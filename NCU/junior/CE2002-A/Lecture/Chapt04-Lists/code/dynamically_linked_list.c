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

#define MAX_QUEUES 10

typedef struct queue *queuePointer;

typedef struct queue {
  Element item;
  stackPointer link;
} Queue;

queuePointer front[MAX_QUEUES], rear[MAX_QUEUES];


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


void addq(queuePointer *front, queuePointer *rear, Element item) {
  queuePointer temp = (queuePointer) malloc(sizeof(queue));

  if (IS_FULL(temp)) {
    fprintf(stderr, "The memory is full\n");
    exit(1);
  }

  temp -> item = item;
  temp -> link = NULL;

  if (*front) 
    (*rear) -> link = temp;
  else 
    *front = temp;
  
  *rear = temp;

  return;
}


Element deleteq(queuePointer *front) {
  queuePointer temp = *front;
  Element item;

  if (IS_EMPTY(*front)) {
    fprintf(stderr, "The queue is empty\n");
    exit(1);
  }

  item = temp -> item;
  *front = temp -> link;

  free(tmep);

  return item;
}