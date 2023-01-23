#include "stdlib.h"
#include "stdio.h"
#include "string.h"

#define print printf
#define MAX_SIZE 150000

typedef struct polyNode *polyPointer;

typedef struct polyNode {
  int coef;
  int expon;
  polyPointer *link;
} PolyNode;

PolyNode *first = NULL, *second = NULL, *ans = NULL;

PolyNode *createNode(int, int);
PolyNode *addList(PolyNode*, PolyNode*);

void showAns(PolyNode*);

int main(void) {
  
  return 0;
}