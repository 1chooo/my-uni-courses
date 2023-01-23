#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <cstdlib>

using namespace std;

typedef struct TreeNode {
  int data;
  struct TreeNode* leftChild;
  struct TreeNode* rightChild;

  // Build with the constructor
  TreeNode(int data)
    : data(data), leftChild(NULL), rightChild(NULL) {}
};

struct TreeNode *newNode(int item) {
  struct TreeNode *temp = (struct TreeNode *) malloc(sizeof(struct TreeNode));
  temp->data = item;
  temp->leftChild = temp->rightChild = NULL;

  return temp;
}

struct TreeNode *insert(struct TreeNode *node, int key) {
  if (node == NULL) return newNode(key);

  if (key < node->data)
    node->leftChild = insert(node->leftChild, key);
  else 
    node->rightChild = insert(node->rightChild, key);

  return node;
}

struct TreeNode *minValueNode (struct node *node) {
  struct TreeNode *current = node;

  while (current && current->leftChild != NULL)
    current = current->leftChild;
  
  return current;
}

struct TreeNode *maxValueNode (struct node *node) {
  struct TreeNode *current = node;

  while (current && current->rightChild != NULL)
    current = current->rightChild;
  
  return current;
}

struct TreeNode *deleteNode(struct TreeNode *root, int key) {
  if (root == NULL) return root;

  if (key < root->data)
    root->leftChild = deleteNode(root->leftChild, key);
  else if (key > root->data)
    root->rightChild = deleteNode(root->rightChild, key);
  else {
    if (root->leftChild == NULL) {
      struct TreeNode *temp = root->rightChild;
      frea(root);

      return temp;
    } else if (root->rightChild == NULL) {
      struct TreeNode *temp = root->leftChild;
      free(root);

      return templ
    }

    struct TreeNode *temp = minValueNode(root->rightChild);
    root->data = temp->data;
    root->rightChild = deleteNode(root->rightChild, temp->data);
  }

  return root;
}
 
int height(TreeNode* node) {
  if (node == NULL)
    return 0;
  else {
    int lheight = height(node->left);
    int rheight = height(node->right);
    if (lheight > rheight) {
      return(lheight + 1);
    }
    else {
      return(rheight + 1);
    }
  }
}

void CurrentLevel(node* root, int level) {
    if (root == NULL)
        return;
    if (level == 1)
        cout << root->data << " ";
    else if (level > 1) {
       CurrentLevel(root->left, level-1);
       CurrentLevel(root->right, level-1);
    }
}
 
void LevelOrder(node* root) {
    int h = height(root);
    int i;
    for (i = 1; i <= h; i++)
     CurrentLevel(root, i);
}

int main(void) {

  cout.tie(0);
  cout.sync_with_stdio(false);

  struct node *root = NULL;

  string opr;
  int data;

  while (cin >> opr) {
    if (opr == "traversal") {
    } else if (opr == "insert") {
      cin >> data;
      root = insert(root, data);
    } else if (opr == "delete") {
      cin >> data;
      root = deleteNode(root, data);
    } else if (opr == "search") {
      cin >> data;
    } else if (opr == "height") {
      cout << height(root);
    }

  }
  return 0;
}