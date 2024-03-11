#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 1000

typedef struct node {
  int data;
  struct node *leftChild, *rightChild;
} Node;