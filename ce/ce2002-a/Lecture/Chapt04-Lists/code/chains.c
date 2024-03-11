#include "stdio.h"
#include "stdlib.h"

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef struct listNode, *listPointer;

typedef struct listNode {
  char data;
  listPointer link;
} ListNode;

listPointer invert(listPointer lead) {
  listPointer middle, trail;
  middle = NULL;

  while (lead) {
    trail = middle;
    middle = lead;
    lead = lead -> link;
    middle -> link = trail;
  }

  return middle;
}

listPointer concatenate(listPointer ptr1, listPointer ptr2) {
  listPointer temp;

  if (IS_EMPTY(ptr1)) {
    return ptr2;
  } else {
    if (!IS_EMPTY(ptr2)) {
      for (temp = ptr1; temp -> link; temp = temp -> link;)
        ;
      temp -> link = ptr2;
    }

    return ptr1;
  }
}


void insertFront(listPointer *ptr, listPointer node) {
  if (IS_EMPTY(*ptr)) {
    *ptr = node;
    node -> link = node;
  } else {
    node -> link = (*ptr) -> link;
    (*ptr) -> link = node;
  }

  return;
}

int length(listPointer ptr) {
  listPointer temp;
  int count = 0;

  if (ptr) {
    temp = ptr;

    do {
      count++;
      temp = temp -> link;
    } while (temp != ptr);
  }

  return count;
}