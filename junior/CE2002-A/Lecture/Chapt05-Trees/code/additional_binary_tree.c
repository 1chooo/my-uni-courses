#include "stdio.h"
#include "stdlib.h"

#define MAX_STACK_SIZE 1000
#define MAX_QUEUE_SIZE 1000

#define IS_EMPTY(ptr) (!(ptr))
#define IS_FULL(ptr) (!(ptr))

typedef enum {not, and, or, true, false} logical;
typedef struct node *tree_pointer;
typedef struct node {
  logical data;
  short int value;
  tree_pointer left_child;
  tree_pointer right_child;
} Node;

for (all 2^n possible combinations) {
  generate the next combination;
  replace the variables by their values;
  evaluate root by traversing it in postorder;
  if (root->value) {
    printf(<combination>);

    return;
  }
}

printf("No satisfiable combination\n");


void post_order_eval(tree_pointer node) {

  /* 
   modified post order traversal to evaluate a 
   propositional calculus tree.
  */

  if (node) {
    post_order_eval(node->left_child);
    post_order_eval(node->right_child);
    
    switch (node->data)
    {
    case not :
      node->value = !node->right_child->value;
      break;
    case and :
      node->value = node->right_child->value && node->left_child->value;
      break;
    case or :
      node->value = node->right_child->value || node->right_child->value;
      break;
    case true :
      node->value = TRUE;
      break;
    case false :
      node->value = FALSE;
      break;
    default:
      break;
    }
  }
}