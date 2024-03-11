#include "stdlib.h"
#include "stdio.h"
#include "alloca.h"

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef struct listNode *listPointer;

typedef struct listNode {
  char data[4];
  listPointer link;
} ListNode;

listPointer ptr = NULL;

listPointer create2() {
  listPointer first, second;
  first = (listPointer) malloc(sizeof(ListNode));
  second = (listPointer) malloc(sizeof(ListNode));

  second -> link = NULL;
  second -> data = 20;
  first -> data = 10;
  first -> link = second;

  return first;
}


void insert(listPointer *ptr, listPointer node) {
  listPointer temp;
  temp = (listPointer) malloc(sizeof(listNode));

  if (IS_FULL(temp)) {
    printf(stderr, "The memory is full.\n");
    exit(1);
  }

  temp -> data = 50;

  if (*ptr) {
    temp -> link = node -> link;
    node -> link = temp;
  } else {
    temp -> link = NULL;
    *ptr = temp;
  }

  return;
}


void delete(listPointer *ptr, listPointer trail, listPointer node) {
  if (trail) {
    trail -> link = node -> link;
  } else {
    *ptr = (*ptr) -> link;
  }

  free(node);

  return;
}


void printList(listPointer ptr) {
  printf("The list contains: ");
  for (; ptr; ptr = ptr -> link)
    printf("%4d", ptr -> data);
  printf("\n");

  return;
}