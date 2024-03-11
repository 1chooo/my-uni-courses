#include "stdio.h"
#include "stdlib.h"

#define MAX_QUEUE_SIZE 100

typedef struct element {
  int key;
} Element;

element queue[MAX_QUEUE_SIZE];
int rear = -1;
int front = -1;

void addq(int *rear, Element item) {
  if (*rear == MAX_QUEUE_SIZE - 1) {
    queue_full();
    
    return;
  }

  queue[++ *rear] = item;
}

Element deleteq(int *front, int rear) {
  if (*front == rear)
    return queue_empty();

  return queue[++ *front];
}