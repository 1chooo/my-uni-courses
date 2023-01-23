// Binary Search Tree operations in C++

#include <iostream>
#include <queue>
using namespace std;

struct node {
  int key;
  struct node *left, *right;
};

// Create a node
struct node *newNode(int item) {
  struct node *temp = (struct node *)malloc(sizeof(struct node));
  temp->key = item;
  temp->left = temp->right = NULL;
  return temp;
}

// Inorder Traversal
void inorder(struct node *root) {
  if (root != NULL) {
    // Traverse left
    inorder(root->left);

    // Traverse root
    cout << root->key << " -> ";

    // Traverse right
    inorder(root->right);
  }
}

// Insert a node
struct node *insert(struct node *node, int key) {
  // Return a new node if the tree is empty
  if (node == NULL) return newNode(key);

  // Traverse to the right place and insert the node
  if (key < node->key)
    node->left = insert(node->left, key);
  else
    node->right = insert(node->right, key);

  return node;
}

// Find the inorder successor
struct node *minValueNode(struct node *node) {
  struct node *current = node;

  // Find the leftmost leaf
  while (current && current->left != NULL)
    current = current->left;

  return current;
}

// Deleting a node
struct node *deleteNode(struct node *root, int key) {
  // Return if the tree is empty
  if (root == NULL) {
    cout << "cannot delete\n"; 
    return root;
  }

  // Find the node to be deleted
  if (key < root->key)
    root->left = deleteNode(root->left, key);
  else if (key > root->key)
    root->right = deleteNode(root->right, key);
  else {
    // If the node is with only one child or no child
    if (root->left == NULL) {
      struct node *temp = root->right;
      free(root);
      return temp;
    } else if (root->right == NULL) {
      struct node *temp = root->left;
      free(root);
      return temp;
    }

    // If the node has two children
    struct node *temp = minValueNode(root->right);

    // Place the inorder successor in position of the node to be deleted
    root->key = temp->key;

    // Delete the inorder successor
    root->right = deleteNode(root->right, temp->key);
  }
  return root;
}

int height(struct node *node) {
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

// /* Print nodes at a current level */
// void printCurrentLevel(node* root, int level) {
//   if (root == NULL)
//     return;
//   if (level == 1)
//     cout << root->key << " ";
//   else if (level > 1) {
//     printCurrentLevel(root->left, level - 1);
//     printCurrentLevel(root->right, level - 1);
//   }
// }

// void printLevelOrder(node* root) {
//   int h = height(root);
//   int i;
//   for (i = 1; i <= h; i++)
//     printCurrentLevel(root, i);
// }

void printLevelOrder(node* root)
{
    // Base Case
    if (root == NULL)
        return;
 
    // Create an empty queue for level order traversal
    queue<node*> q;
 
    // Enqueue Root and initialize height
    q.push(root);
 
    while (q.empty() == false) {
        // Print front of queue and remove it from queue
        node* node = q.front();
        cout << node->key << " ";
        q.pop();
 
        /* Enqueue left child */
        if (node->left != NULL)
            q.push(node->left);
 
        /*Enqueue right child */
        if (node->right != NULL)
            q.push(node->right);
    }
}
 

// Driver code
int main() {
  struct node *root = NULL;

  string opr;
  int data;

  while (cin >> opr) {
    if (opr == "traversal") {
      // cout << "Inorder traversal: ";
      // inorder(root);
      // LevelOrder(root);
      printLevelOrder(root);
      cout << endl;
    } else if (opr == "insert") {
      cin >> data;
      root = insert(root, data);
    } else if (opr == "delete") {
      cin >> data;
      root = deleteNode(root, data);
    } 
    // else if (opr == "search") {
    //   cin >> data;
    // } 
    else if (opr == "height") {
      cout << height(root) << endl;
    }

  }
  // root = insert(root, 8);
  // root = insert(root, 3);
  // root = insert(root, 1);
  // root = insert(root, 6);
  // root = insert(root, 7);
  // root = insert(root, 10);
  // root = insert(root, 14);
  // root = insert(root, 4);

  // cout << "Inorder traversal: ";
  // inorder(root);

  // cout << "\nAfter deleting 10\n";
  // root = deleteNode(root, 10);
  // cout << "Inorder traversal: ";
  // inorder(root);
}

// insert 1
// insert 3
// insert 7
// insert -1
// height
// insert 9
// insert 2
// delete -1
// delete 3
// height
// traversal