#include "stdlib.h"
#include "stdio.h"
#include "string.h"

#define MAX_ELEMENTS 200 /* maximum heap size + 1 */
#define HEAP_FULL(n) (n == MAX_ELEMENTS - 1)
#define HEAP_EMPTY(n) (!n)

typedef struct element {
  int key;
  /* other fields */
} Element;

Element heap[MAX_ELEMENTS];
int n = 0;

void insert_max_heap(Element, int*);

void insert_max_heap(Element item, int *n) {

  /*
    insert item into a max heap
    of current size *n
  */

  int i;
  if (HEAP_FULL(*n)) {
    fprintf(stderr, "The heap is full. \n");
    exit(1);
  }

  i = ++(*n);
  while ((i != 1) && (item.key > heap[i / 2].key)) {
    heap[i] = heap[i / 2];
    i /= 2;
  }

  heap[i] = item;
}

Element delete_heap(int *n) {

  /*
    delete element with the higheset key
    from the heap
  */

  int parent, child;
  Element item, temp;

  if (HEAP_EMPTY(*n)) {
    fprintf(stderr, "The heap is empty\n.");
    exit(1);
  }

  /*
    save value of the element with the highest key.
  */
  item = heap[1];

  /* use last element in heap to adjust heap */
  temp = heap[(*n)--];
  parent = 1;
  child = 2;

  while (child <= *n) {
  
    /* find the largest child of the current parent */
    if ((child < *n) && (heap[child].key < heap[child + 1].key))
      child++;

    if (temp.key >= heap[child].key)
      break;
    
    /* move to the next lower level */
    heap[parent] = heap[child];
    parent = child;
    child *= 2;
  }

  heap[parent] = temp;

  return item;
}