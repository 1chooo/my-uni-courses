#include "stdio.h"
#include "stdlib.h"
#include <string.h>

typedef struct treeNode {
  int data;
  struct treeNode *leftChild, *rightChild;
} TreeNode;
void inorder(treePointer), preorder(treePointer), postorder(treePointer);
// typedef struct Node Tree;
// typedef struct Node *TreePointer;

Node *newNode(int data) {
  Node tempNode = (Node *) malloc(sizeof(Node));

  tempNode->data = data;
  tempNode->leftChild = NULL;
  tempNode->rightChild = NULL;

  return tempNode;
}

// Node *createNode(int index, int num) {
//   Node *newNode = (Node *) malloc(sizeof(Node));

//   if (index < num) {
//     root = newNode(stack[index]);
//     root->leftChild = createTree(2 * index + 1, num);
//     root->rightChild = createTree(2 * index + 2, num);
//   }

//   return newNode;
// }


#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 1000

typedef struct node {
  int data;
  struct node *leftChild, *rightChild;
} Node;

Node *createTreeNode(int); 
Node *createTree(int *, int, int);

void inorder(Node*);
void preorder(Node*);
void postorder(Node*);


// void resetMemory();

int main(void) {
  int N;
  int M;
  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    scanf("%d", &M);
    int stack[M];

    if (M == 0) {
      return 0;
    }

    for (int j = 0; j <= M; j++) {
      scanf("%d", &stack[i]);
    }

    for (int j = 0; j <= M; j++) {
      printf("%d ", stack[i]);
    }
    printf("\n");

    Node* root = createTree(stack, 0, M);

    preorder(root);
    printf("\n");

    inorder(root);
    printf("\n");

    postorder(root);
    printf("\n");

    free(root);

    // resetMemory();
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

Node *createTree(int *stack, int index, int num) {
  Node *root = NULL;

  if (index < num) {
    root = createTreeNode(stack[index]);
    root->leftChild = createTree(stack, 2 * index + 1, num);
    root->rightChild = createTree(stack, 2 * index + 2, num);
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

// void resetMemory() {
//   memset(stack, 0, sizeof(stack));

//   for(size_t i = 0; i < sizeof stack; ++i)
//     stack[i] = 0;
  
//   return;
// }