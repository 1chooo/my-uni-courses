#include <bits/stdc++.h>
using namespace std;

typedef struct node
{
  int data;
  struct node *left, *right;
  node(int data) : data(data), left(NULL), right(NULL){};
} node;
typedef node *link;

link bst = NULL;
int counter;

void insert_bst(int data, link *p = &bst)
{
  if (!(*p))
    *p = new node(data);
  else if (data < (*p)->data)
    insert_bst(data, &((*p)->left));
  else
    insert_bst(data, &((*p)->right));
}

void delete_bst(int data, link *p = &bst)
{
  if (!(*p))
    cout << "cannot delete" << endl;
  else if ((*p)->data == data)
  {
    if ((*p)->left && (*p)->right)
    {
      link *temp = &((*p)->left);
      while ((*temp)->right)
        temp = &((*temp)->right);
      (*p)->data = (*temp)->data;
      (*temp) = (*temp)->left;
    }
    else if ((*p)->left)
      *p = (*p)->left;
    else if ((*p)->right)
      *p = (*p)->right;
    else
      *p = NULL;
  }
  else if (data < (*p)->data)
    delete_bst(data, &((*p)->left));
  else
    delete_bst(data, &((*p)->right));
}

void traversal()
{
  queue<link> q;
  if (bst)
    q.push(bst);
  while (!q.empty())
  {
    node *temp = q.front();
    q.pop();
    cout << temp->data << " ";
    if (temp->left)
      q.push(temp->left);
    if (temp->right)
      q.push(temp->right);
  }
  cout << endl;
}

int height(link p = bst)
{
  if (!p)
    return 0;
  return 1 + max(height(p->left), height(p->right));
}

void search_i(link p = bst)
{
  if (p->left && counter > 0)
    search_i(p->left);
  if (!--counter)
    cout << p->data;
  if (p->right && counter > 0)
    search_i(p->right);
}

int main()
{
  string command;
  int data;
  while (cin >> command)
  {
    if (command == "insert")
    {
      cin >> data;
      insert_bst(data);
    }
    else if (command == "delete")
    {
      cin >> data;
      delete_bst(data);
    }
    else if (command == "search")
    {
      cin >> counter;
      search_i(bst);
      cout << endl;
    }
    else if (command == "height")
      cout << height() << endl;
    else if (command == "traversal")
    {
      traversal();
      break;
    }
  }
  return 0;
}