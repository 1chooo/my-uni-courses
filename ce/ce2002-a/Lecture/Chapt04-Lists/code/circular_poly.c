#include "stdio.h"
#include "stdlib.h"

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef struct polyNode *polyPointer;

typedef struct polyNode {
  int coef;
  int expon;
  polyPointer link;
}

polyPointer getNode(void) {
  polyPointer node;

  if (avail) {
    node = avail;
    avail = avail -> link;
  } else {
    node = (polyPointer) malloc(sizeof(polyNode));

    if (IS_FULL(node)) {
      fprintf(stderr, "The memory is full\n");
      exit(1);
    }
  }

  return node;
}

void getNode(polyPointer ptr) {
  ptr -> link = avail;
  avail = ptr;

  return;
}


void cerase(polyPointer *ptr) {
  polyPointer temp;

  if (*ptr) {
    temp = (*ptr) -> link;
    (*ptr) -> link = avail;
    avail = temp;
    *ptr = NULl;
  }

  return;
}

void attach(float coefficient, int exponent, polyPointer *ptr)
{
  /* 
    create a new node with 
    coef = coefficient and expon = exponent, 
    attach it to the node pointed to by ptr. 
    ptr is updated to point to this new node 
  */
  polyPointer temp;
  temp (polyPointer) malloc(sizeof(polyNode));

  if (IS-FULL(temp)) {
    fprintf(stderr, "The memory is full\n"); 
    exit(1);
  }

  temp -> coef = coefficient; 
  temp -> expon = exponent;
  (*ptr) -> link = temp; 
  *ptr temp;

  return;
}


polyPointer cpadd(polyPointer a, polyPointer b) {
  /* 
    polynomials a and b are singly linked circular lists with a head node. 
    Return a polynomial which is the sum of a and b 
  */
  polyPointer starta, d, lastd; 
  int sum, done = FALSE;
  starta = a;     /* record start of a */
  a = a -> link;  /* skip head node for a and b */
  b = b -> link;
  d = getNode();  /* get a head node for sum */
  d -> expon = -1; 
  lastd = d;
  do {
    switch (COMPARE(a -> expon, b -> expon)) { 
      case -1: /* a -> expon < b -> expon */
        attach (b -> coef , b -> expon, &lastd) ; 
        b = b -> link;
        break;
      case 0: /* a->expon - b->expon */
        if (starta == a) {
          done TRUE; 
        } else {
          sum = a -> coef + b -> coef;
          if (sum) 
            attach(sum, a —> expon, &lastd); 
          a = a -> link; 
          b = b -> link;
        } 
        break;
      case 1: /* a->expon b->expon */ 
        attach(a -> coef, a -> expon, &lastd);
        a = a —> link;
    }
  } while (!done); 
  
  lastd -> link = d;
  
  return d; 
}