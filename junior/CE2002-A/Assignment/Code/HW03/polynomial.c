// segmentation fault

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_SIZE 150000
#define print printf

typedef struct polyNode {
  int coef;
  int expon;
  struct polyNode *next;
} PolyNode; 

PolyNode *createNode(int, int);
PolyNode *linkNode(PolyNode*, PolyNode*, int);
PolyNode *addList(PolyNode*, PolyNode*);

void showAns(PolyNode*);

int main(void) {
  int N, M;
  PolyNode *first = NULL, *second = NULL, *ans = NULL;
  PolyNode *temp = NULL;

  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    int coef, expon;

    scanf("%d %d", &coef, &expon);
    temp = createNode(coef, expon);

    linkNode(first, temp, i);
  }

  scanf("%d", &M);
  for (int i = 0; i < M; i++) {
    int coef, expon;

    scanf("%d %d", &coef, &expon);
    temp = createNode(coef, expon);

    linkNode(second, temp, i);
  }

  ans = addList(first, second);
  showAns(ans);

  free(first); free(second); free(ans);

  return 0;
}

PolyNode *createNode(int coef, int expon) {

  PolyNode *newNode = (PolyNode *) malloc(sizeof(PolyNode));

  newNode->coef = coef;
  newNode->expon = expon;
  newNode->next = NULL;

  return newNode;
}


PolyNode *linkNode(PolyNode *polynomial, PolyNode* node, int index) {

  PolyNode *temp = NULL, *lastNode = NULL;

  temp = node;

  if (index == 0) {
    polynomial = temp;
    lastNode = temp;
  } else {
    lastNode->next = temp;
    lastNode = temp;
  }

  return polynomial;
}

PolyNode *addList(PolyNode *first, PolyNode *second) {
  PolyNode *ans = NULL;
  PolyNode *temp = NULL;

  while (first && second) {
    if (first->expon > second->expon) {
      if (!ans) {
        ans = createNode(first->coef, first->expon);
        temp = ans;
      } else {
        temp->next = createNode(first->coef, first->expon);
        temp = temp->next;
      }

      first = first->next;
    } else if (first->expon < second->expon) {
      if (!ans) {
        ans = createNode(second->coef, second->expon);
        temp = ans;
      }
      else {
        temp->next = createNode(second->coef, second->expon);
        temp = temp->next;
      }

      second = second->next;
    } else { /* first equal to second. */
      if (!ans) {
        ans = createNode((first->coef + second->coef), first->expon);
        temp = ans;
      } else {
        temp->next = createNode((first->coef + second->coef), first->expon);
        temp = temp->next;
      }

      first = first->next;
      second = second->next;
    }
  }

  while (first) {
    temp->next = createNode(first->coef, first->expon);
    temp = temp->next;
    first = first->next;
  }

  while (second) {
    temp->next = createNode(second->coef, second->expon);
    temp = temp->next;
    second = second->next;
  }

  return ans;
}


void showAns(PolyNode *ans) {
  while (ans) {
    if (ans->coef != 0) {
      print("%d %d ", ans->coef, ans->expon);
    }
    ans = ans->next;
  }
  print("\n");

  return;
}