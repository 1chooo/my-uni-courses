#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <sstream>
#include <cstdlib>

#define Max_Size 1000

using namespace std;

typedef struct BSTNode {
  int data;
  struct BSTNode *left, *right;

  BSTNode (int data) 
    : data(data), left(NULL), right(NULL) {};
} BSTNode;

// void *insert(BSTNode*, int);
// int getHeight(BSTNode*);
// void traversal(BSTNode*);
// BSTNode *getMaximum(BSTNode*);
// BSTNode *getMinimum(BSTNode*);
// BSTNode *search(BSTNode*, int, BSTNode*);
// void *Delete(BSTNode*, int);
// vector<int> Inorder(BSTNode*, vector<int> &);
// void find_nth_minimum(BSTNode*, int);





void insert(BSTNode *&root, int data) {
  BSTNode *node = new BSTNode(data);

  if (!root) {
    root = node;

    return;
  }

  BSTNode *last = NULL;
  BSTNode *temp = root;

  while (temp) {
    if (temp->data > data) {
      last = temp;
      temp = temp->left;
    } else if (temp->data < data) {
      last = temp;
      temp = temp->right;
    }
  }

  if (last->data > data)
    last->left = node;
  else
    last->right = node;

  // return;
}

void traversal(BSTNode *root) {

  if (!root)
    return;

  queue<BSTNode*> BSTQueue;
  BSTQueue.push(root);

  while (!BSTQueue.empty()) {
    BSTNode *local = BSTQueue.front();
    BSTQueue.pop();
    cout << local->data << " ";

    if (local->left)
      BSTQueue.push(local->left);

    if (local->right)
      BSTQueue.push(local->right);
  }

  cout << endl;
  return;
}

int getHeight(BSTNode *root) {
  int height = 0;

  if (!root)
    return height;

  queue<BSTNode*> BSTQueue;
  BSTQueue.push(root);

  while (!BSTQueue.empty()) {

    int size = BSTQueue.size();

    for (int i = 0; i < size; i++) {
      BSTNode *temp = BSTQueue.front();
      BSTQueue.pop();

      if (temp->left)
        BSTQueue.push(temp->left);

      if (temp->right)
        BSTQueue.push(temp->right);
    }
    height++;
  }

  return height;
}

BSTNode *getMaximum(BSTNode* local) {
  while (local->right)
    local = local->right;

  return local;
}


BSTNode *getMinimum(BSTNode* local) {
  while (local->left)
    local = local->left;

  return local;
}


BSTNode *search(BSTNode *local, int data, BSTNode *last) {

  while (local && data != local->data) {
    last = local;

    if (data < local->data)
      local = local->left;
    else if (data > local->data)
      local = local->right;
  }

  return local;
}


void Delete(BSTNode *&root, int data) {
  BSTNode *last = NULL;
  BSTNode *local = root;

  search(local, data, last);

  if (local == NULL) {
    cout << "cannot delete\n";
    return;
  }

  if (local->left == NULL && local->right == NULL) {

    if (local != root) {
      if (last->left == local)
        last->left = NULL;
      else
        last->right = NULL;
    } else
      root = NULL;

    delete (local);
  } else if (local->left && local->right) {
    BSTNode *predecessor = getMaximum(local->left);

    int val = predecessor->data;
    Delete(root, val);
    local->data = val;
  } else {
    BSTNode *child;

    if (local->left)
      child = local->left;
    else
      child = local->right;

    if (local != root) {
      if (local == last->left)
        last->left = child;
      else
        last->right = child;
    } else {
      root = child;
    }

    delete (local);
  }
}


vector<int> Inorder(BSTNode *root, vector<int> &dataset) {

  if (root != NULL) {
    Inorder(root->left, dataset);
    dataset.push_back(root->data);
    Inorder(root->right, dataset);
  }

  return dataset;
}

void find_nth_minimum(BSTNode *root, int n) {

  if (!root) return;

  vector<int> dataset;
  dataset = Inorder(root, dataset);
  int nth_minimum_val = dataset[n - 1];
  cout << nth_minimum_val << '\n';
}


int main(void) {

  cout.tie(0);
  cout.sync_with_stdio(false);

  string opr;
  BSTNode *root = NULL;
  vector<int> dataset;
  dataset.reserve(1009);

  int data;

  // while (cin >> opr) {

  //   switch (opr)
  //   {
  //   case "insert" :
  //     cin >> data;
  //     insert(root, data);
  //     break;
  //   case "delete" :
  //     cin >> data;
  //     delete(root, data);
  //     break;
  //   case "search" :
  //     find_nth_minimum(root, data);
  //     break;
  //   case "height" :
  //     cout << getHeight(root) << endl;
  //     break;
  //   case "traversal" :
  //     traversal(root);
  //     break;
  //   default:
  //     break;
  //   }
  // }

  while(cin >> opr){
    if (opr == "insert") {
      cin >> data;
      insert(root, data);
    } else if (opr == "delete") {
      cin >> data;
      Delete(root, data);
    } else if (opr == "search") {
      cin >> data;
      find_nth_minimum(root, data);
      // cout << endl;
    } else if (opr == "height") {
      cout << getHeight(root) << endl;
    } else if (opr == "traversal") {
      traversal(root);
      break;
    }
  }

  return 0;
}