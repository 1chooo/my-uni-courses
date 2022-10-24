#include "stdio.h"
#include "stdlib.h"

#define MAX_QUEUE_SIZE 100

typedef struct element {
  int key;
} Element;

Element queue[MAX_QUEUE_SIZE];

void addq(int front, int *rear, Element item) {
  *rear = (*rear + 1) % MAX_QUEUE_SIZE;

  if (front == *rear) {
    queue_full(rear);

    return;
  }

  queue[*rear] = item;
}

void queue_empty() {
  return;
}

Element deleteq(int *front, int rear) {
  Element item;

  if (*front == rear) 
    return queue_empty();
  
  *front = (*front + 1) % MAX_QUEUE_SIZE;

  return queue[*front];
}