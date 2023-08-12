#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define MAX_STACK_SIZE 10009

typedef struct node {
  int data;
  struct node *leftChild, *rightChild;
} Node;

Node *createTreeNode(int);

int main(void) {
  int height, nums = 1;
  char temp[1009];
  char treeMember[10009];

  scanf("%d", &height);

  nums = pow(2, height) - 1;

  for (int i = 0; i < nums; i++) {
    scanf("%s", &temp);
    treeMember[i] = temp;
    print("%s\n", treeMember[i]);
  }


  return 0;
}

Node *createTreeNode(int data) {
  Node *treeNode = (Node *) malloc(sizeof(Node));

  treeNode->data = data;
  treeNode->leftChild = NULL;
  treeNode->rightChild = NULL;

  return treeNode;
}