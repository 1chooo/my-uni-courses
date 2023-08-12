#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_STACK_SIZE 1000

typedef struct node {
  int data;
  struct node *leftChild, *rightChild;
} Node;

Node *createTreeNode(int); 
Node *createTree(int [], int, int);

void inorder(Node*);
void preorder(Node*);
void postorder(Node*);

void resetMemory();

int main(void) {
  int N;
  int M;
  scanf("%d", &N);

  for (int i = 1; i <= N; i++) {
    scanf("%d", &M);

    if (M == 0) {
      return 0;
    }

    int stack[M];

    for (int j = 0; j < M; j++) {
      scanf("%d", &stack[j]);
    }

    Node* root = createTree(stack, 0, M);

    preorder(root);
    printf("\n");

    inorder(root);
    printf("\n");

    postorder(root);
    printf("\n");

    free(root);
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

Node *createTree(int stack[], int index, int num) {
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
