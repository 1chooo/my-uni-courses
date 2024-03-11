#include <bits/stdc++.h>
using namespace std;

struct Node
{
  int data;
  Node *left;
  Node *right;
};

Node *newnode(int data)
{
  Node *node = (Node *)malloc(sizeof(Node));
  node->data = data;
  node->left = node->right = NULL;
  return node;
}

Node *insert(int arr[], int i, int n)
{
  Node *root = nullptr;
  if (i < n)
  {
    root = newnode(arr[i]);
    root->left = insert(arr, 2 * i + 1, n);
    root->right = insert(arr, 2 * i + 2, n);
  }
  return root;
}

void preorder(Node *root)
{
  if (root != NULL)
  {
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
  }
}

void inorder(Node *root)
{
  if (root != NULL)
  {
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
  }
}

void postorder(Node *root)
{
  if (root != NULL)
  {
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " ";
  }
}

int main()
{
  // freopen("test.in", "r", stdin);
  // freopen("test.out", "w", stdout);
  ios::sync_with_stdio(0);
  cin.tie(0);

  int case_num;
  cin >> case_num;
  while (case_num != 0)
  {
    int size;
    cin >> size;
    int arr[size];

    for (int i = 0; i < size; i++)
    {
      cin >> arr[i];
    }
    int n = sizeof(arr) / sizeof(arr[0]);
    Node *root = insert(arr, 0, n);
    preorder(root);
    cout << '\n';
    inorder(root);
    cout << '\n';
    postorder(root);
    cout << '\n';
    case_num--;
  }

  return 0;
}