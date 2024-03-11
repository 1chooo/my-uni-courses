#include "stdlib.h"
#include "stdio.h"

#define MAX_STACK_SIZE 100

typedef struct offsets {
  short int vert;
  short int horiz;
} Offsets;

Offsets move[8];

typedef struct element {
  short int row;
  short int col;
  short int dir;
} Element;

Element stack[MAX_STACK_SIZE];

