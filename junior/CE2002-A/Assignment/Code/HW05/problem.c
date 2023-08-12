// This code will runtime-error.
// 原本是宣告 Global 的 stack, 最後也有清空記憶體, 不過還是出問題

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 1009

typedef struct node {
  int data;
  struct node *leftChild, *rightChild;
} Node;

Node *createTreeNode(int); 
Node *createTree(int, int);

void inorder(Node*);
void preorder(Node*);
void postorder(Node*);

void resetMemory();

int stack[MAX_STACK_SIZE];

int main(void) {
  int N;
  int M;
  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    scanf("%d", &M);

    if (M == 0) {
      return 0;
    }

    for (int j = 0; j < M; j++) {
      scanf("%d", &stack[j]);
    }

    Node* root = createTree(0, M);

    preorder(root);
    printf("\n");

    inorder(root);
    printf("\n");

    postorder(root);
    printf("\n");

    free(root);

    resetMemory();
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

Node *createTree(int index, int num) {
  Node *root = NULL;

  if (index < num) {
    root = createTreeNode(stack[index]);
    root->leftChild = createTree(2 * index + 1, num);
    root->rightChild = createTree(2 * index + 2, num);
  }

  return root;
}

void preorder(Node *ptr) {   /* preorder tree traversal */
  if (ptr) {
    printf("%d ", ptr->data);
    preorder(ptr->leftChild);
    preorder(ptr->rightChild);
  }

  return;
}

void inorder(Node *ptr) {  /* inorder tree traversal */
  if (ptr) {
    inorder(ptr->leftChild);
    printf("%d ", ptr->data);
    inorder(ptr->rightChild);
  }

  return;
}


void postorder(Node *ptr) {   /* postorder tree traversal */
  if (ptr) {
    postorder(ptr->leftChild);
    postorder(ptr->rightChild);
    printf("%d ", ptr->data);
  }

  return;
}

void resetMemory() {
  memset(stack, 0, sizeof(stack));

  // sizeof will be considered as the operator.
  // for(size_t i = 0; i < sizeof stack; ++i)
  //   stack[i] = 0;
  
  return;
}