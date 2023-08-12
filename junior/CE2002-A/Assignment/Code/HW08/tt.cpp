#include <bits/stdc++.h>
using namespace std;

int arr[1005];
int flag = 0;

struct Node
{
  int data;
  Node *leftNode = NULL;
  Node *rightNode = NULL;
};

Node *BST = NULL;

Node *insert(Node *node, int n);
int height(Node *node);
void output(Node *node, int level);
void traversal(Node *node);
void inorder(int i);
void search(Node *node);
int getMax(Node *node);
void remove(int key);

int main()
{
  string input;

  while (cin >> input)
  {
    if (input == "insert")
    {
      int num;
      cin >> num;
      if (BST == NULL)
      {
        Node *tmp = new Node;
        tmp->data = num;
        BST = tmp;
      }
      else
        insert(BST, num);
    }
    else if (input == "height")
    {
      int h = height(BST);
      cout << h << '\n';
    }
    else if (input == "search")
    {
      int i;
      cin >> i;
      search(BST);
      cout << arr[i - 1] << '\n';
      flag = 0;
    }
    else if (input == "delete")
    {
      int key;
      cin >> key;
      remove(key);
    }
    else if (input == "traversal")
    {
      traversal(BST);
    }
  }
  return 0;
}
Node *insert(Node *node, int n)
{
  if (n > node->data)
  {
    if (node->rightNode == NULL)
    {
      Node *temp1 = new Node;
      temp1->data = n;
      node->rightNode = temp1;
    }
    else
      node->rightNode = insert(node->rightNode, n);
  }
  else if (n < node->data)
  {
    if (node->leftNode == NULL)
    {
      Node *temp2 = new Node;
      temp2->data = n;
      node->leftNode = temp2;
    }
    else
      node->leftNode = insert(node->leftNode, n);
  }
  return node;
}

int height(Node *node)
{
  if (node == NULL)
    return 0;
  else
  {
    int lheight = height(node->leftNode);
    int rheight = height(node->rightNode);
    return max(lheight, rheight) + 1;
  }
}
void output(Node *node, int level)
{
  if (node == NULL)
    return;
  if (level == 1)
    cout << node->data << " ";
  else
  {
    output(node->leftNode, level - 1);
    output(node->rightNode, level - 1);
  }
}

void traversal(Node *node)
{
  int h = height(node);
  if (h == 0)
  {
    cout << '\n';
    return;
  }
  for (int i = 1; i <= h; i++)
    output(node, i);
}

void inorder(int i)
{
  arr[flag] = i;
  flag++;
}

void search(Node *node)
{
  if (node != NULL)
  {
    search(node->leftNode);
    inorder(node->data);
    search(node->rightNode);
  }
}

int getMax(Node *node)
{
  while (node->rightNode != NULL)
    node = node->rightNode;
  return node->data;
}
void remove(int key)
{
  Node *deNode = NULL;
  Node *pre = BST;
  Node *now = BST;
  bool r = false;
  while (now != NULL)
  {
    if (key == now->data)
    {
      deNode = now;
      break;
    }
    else if (key > now->data)
    {
      pre = now;
      now = now->rightNode;
      r = true;
    }
    else
    {
      pre = now;
      now = now->leftNode;
      r = false;
    }
  }
  if (deNode == NULL)
  {
    cout << "cannot delete" << '\n';
    return;
  }
  if (deNode->leftNode != NULL and deNode->rightNode != NULL)
  {
    pre = deNode;
    now = deNode->leftNode;
    int t = getMax(now);
    deNode->data = t;
    while (now->rightNode != NULL)
    {
      pre = now;
      now = now->rightNode;
    }
    if (pre == deNode)
      pre->leftNode = now->leftNode;
    else
      pre->rightNode = now->leftNode;
    return;
  }
  if (deNode->leftNode == NULL and deNode->rightNode != NULL)
  {
    if (deNode == BST)
    {
      BST = deNode->rightNode;
      return;
    }
    if (r)
      pre->rightNode = deNode->rightNode;
    else
      pre->leftNode = deNode->rightNode;
    return;
  }
  if (deNode->leftNode != NULL and deNode->rightNode == NULL)
  {
    if (deNode == BST)
    {
      BST = deNode->leftNode;
      return;
    }
    else
    {
      if (r)
        pre->rightNode = deNode->leftNode;
      else
        pre->leftNode = deNode->leftNode;
    }
    return;
  }
  if (deNode == BST)
  {
    BST = NULL;
    return;
  }
  if (r)
  {
    pre->rightNode = NULL;
    return;
  }
  else
  {
    pre->leftNode = NULL;
    return;
  }
}