#include "stdlib.h"
#include "stdio.h"

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef struct polyNode *polyPointer;

typedef struct polyNode {
  int coef;
  int expon;
  polyPointer link;
}

polyPointer a, b, d;

// coef | expon | link


polyPointer padd(polyPointer a, polyPointer b) {
  /* return a polynomial which is the sum of a and b */ 
  polyPointer front, rear, temp;
  int sum;

  rear = (polyPointer) malloc(sizeof(polyNode)); 

  if (IS_FULL(rear)) {
    fprintf (stderr, "The memory is full\n");
    exit(1); 
  }

  front = rear; 
  
  while (a && b)
    switch (COMPARE(a -> expon, b -> expon)) { 
      case -1: /* a —> expon < b —> expon */
        attach(b -> coef, b -> expon, &rear);
        b = b -> link;
        break;
      case 0:  /* a -> expon = b -> expon */
        sum = a -> coef + b -> coef;
        if (sum)
          attach(sum, a-> expon, &rear);
        a = a -> link;
        b = b -> link;
        break;
      case 1:  /* a -> expon > b -> expon */
        attach(a -> coef, a -> expon, &rear);
        a = a -> link;
    }
  /* copy rest of list a and then list b */
  for (; a; a = a -> link) 
    attach(a -> coef, a -> expon, &rear); 
  for (; b; b = b -> link) 
    attach(b -> coef, b -> expon, &rear); 
    rear -> link NULL;
  /* delete extra initial node */
  temp = front; 
  front = front -> link; 
  free(temp); 
  
  return front;
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


void erase(polyPointer *ptr) {
  polyPointer temp;

  while (*ptr) {
    temp = *ptr;
    *ptr = (*ptr) -> link;

    free(temp);
  } 

  return;
}