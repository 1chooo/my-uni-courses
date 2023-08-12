#include "stdio.h"
#include "stdlib.h"

typedef struct threaded_tree *threaded_pointer;
typedef struct threaded_tree {
  short int left_thread;
  short int right_thread;
  threaded_pointer left_child;
  threaded_pointer right_child;
  char data;
}

threaded_pointer insucc(threaded_pointer);
threaded_pointer tinorder(threaded_pointer);

int main(void) {

  return 0;
}

threaded_pointer insucc(threaded_pointer tree) {

  /* 
   find the inorder sucessor of tree 
   in a threaded binary tree
  */

  threaded_pointer temp;
  temp = tree->right_child;

  if (!tree->right_thread)
    while (!temp->left_thread)
      temp = temp->left_child; 

  return temp;
}

void tinorder(threaded_pointer tree) {

  /*
   traverse the threaded binary tree inorder
  */

  threaded_pointer temp = tree;

  for (;;) {
    temp = insucc(temp);

    if (temp == tree) break;
    printf("%3c", temp->data);
  }
}

void insert_right(threaded_pointer parent, threaded_pointer child) {

  /*
   insert child as the right child of 
   parent in a threaded binary tree.
  */

  threaded_pointer temp;
  child->right_child = parent->right_child;
  child->right_thread = parent->right_thread;
  child->left_child = parent;
  child->left_thread = TRUE;
  parent->right_child = child;
  parent->right_thread = FALSE;

  if (!child->right_thread) {
    temp = insucc(child);
    temp->left_child = child;
  }
}