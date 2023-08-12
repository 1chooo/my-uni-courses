#include "stdio.h"
#include "stdlib.h"

#define MAX_STACK_SIZE 1000
#define MAX_QUEUE_SIZE 1000

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef struct node *tree_pointer;
typedef struct node {
  int data;
  tree_pointer left_child, right_child;
} Node;

void inorder(tree_pointer), preorder(tree_pointer), postorder(tree_pointer);
void iter_inorder(tree_pointer);
void level_order(tree_pointer);

void add(int*, tree_pointer);
Node delete(int*);
void empty_stack(), full_stack();

void addq(int, int*, tree_pointer);
Node deleteq(int*, int);
void empty_queue(), full_queue();

tree_pointer copy(tree_pointer);

int equal(tree_pointer, tree_pointer);

int main(void) {


  return 0;
}

void inorder(tree_pointer ptr) {  /* inorder tree traversal */
  if (ptr) {
    inorder(ptr->left_child);
    printf("%d", ptr->data);
    inorder(ptr->right_child);
  }

  return;
}

void preorder(tree_pointer ptr) {   /* preorder tree traversal */
  if (ptr) {
    printf("%d", ptr->data);
    preorder(ptr->left_child);
    preorder(ptr->right_child);
  }

  return;
}

void postorder(tree_pointer ptr) {   /* postorder tree traversal */
  if (ptr) {
    postorder(ptr->left_child);
    postorder(ptr->right_child);
    printf("%d", ptr->data);
  }

  return;
}

void iter_inorder(tree_pointer node) {
  int top = -1;
  tree_pointer stack[MAX_STACK_SIZE];

  for (;;) { 
    for (; node; node = node->left_child) {
      add(&top, node);    /* add to stack */
    }

    node = delete(&top);  /* delete from stack */

    if (!node) {
      break;              /* empty stack */
    }

    printf("%d", node->data);
    node = node->right_child;
  }

  return;
}


void level_order(tree_pointer ptr) {  /* level order tree traversal */
  int front = 0, rear = 0;
  tree_pointer queue[MAX_QUEUE_SIZE];

  if (!ptr) return;
  addq(front, &rear, ptr);

  for (;;) {
    ptr = deleteq(&front, rear);

    if (ptr) {
      printf("%d", ptr->data);

      if (ptr->left_child) 
        addq(front, &rear, ptr->left_child);

      if (ptr->right_child)
        addq(front, &rear, ptr->right_child);
    } else {
      break;
    }
  }

  return;
}

tree_pointer copy(tree_pointer original) {
  /* this function returns a tree_pointer to an exact copy of the original tree */
  tree_pointer temp;

  if (original) {
    temp = (tree_pointer) malloc(sizeof(Node));

    if (IS_FULL(temp)) {
      fprintf(stderr, "The memory is full\n");
      exit(1);
    }

    temp->left_child = copy(original->left_child);
    temp->right_child = copy(original->right_child);
    temp->data = original->data;

    return temp;
  }

  return NULL;
}

int equal(tree_pointer first, tree_pointer second) {
  /* 
   function returns FALSE if the binary trees first and second 
   are not equal, Otherwise it returns TRUE.
  */

 return ((!first && !second) || 
         (first && second && (first->data == second->data)) &&
         (equal(first->left_child, second->left_child)) &&
         (equal(first->right_child, second->right_child)))
}

/*
 * Still need to debug...
 */
void add(int *top, Node item) {
  if (*top >= MAX_STACK_SIZE) {
    stack_full();

    return;
  }
  stack[++*top] = item;

  return;
}

Node delete(int *top) {
  if (*top == -1)
    return stack_empty();

  return stack[(*top)--];
}

void addq(int *rear, int item) {
  if (*rear == MAX_QUEUE_SIZE - 1) {
    queue_full();
    
    return;
  }

  queue[++ *rear] = item;
}

Node deleteq(int *front, int rear) {
  if (*front == rear)
    return queue_empty();

  return queue[++ *front];
}

void queue_full() {
    fprintf(stderr, "error: stack is full\n");

    return;
}

void queue_empty() {
    fprintf(stderr, "error: stack is empty\n");

    return;
}