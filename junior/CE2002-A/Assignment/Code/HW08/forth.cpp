#include <iostream>
#include <cstdlib>
#include <string>
#include <queue>
using namespace std;
struct node
{
  long long int data;
  struct node *left;
  struct node *right;
};
typedef struct node Node;
bool ifdelete = false;
int numNode = 0;
Node *getnewNode(long long int x)
{
  Node *newnode;
  newnode = (Node *)malloc(sizeof(Node));
  newnode->data = x;
  newnode->left = NULL;
  newnode->right = NULL;
  return newnode;
}
// insert x : 將整數 x 插入 BST 中
Node *insertNode(Node *root, long long int x)
{

  if (!root)
  {
    root = getnewNode(x);
    return root;
  }

  if (x < root->data)
    root->left = insertNode(root->left, x);
  else if (x > root->data)
    root->right = insertNode(root->right, x);

  return root;
}
// delete x : 將 BST 中的 data 為 x 的節點刪除
//若BST中沒有 data 為 x 的節點則輸出cannot delete
//(若刪除的節點有兩個child 則以左子樹中 data 最大的節點取代)
Node *maxValueNode(Node *root)
{
  Node *current = root;

  /* loop down to find the leftmost leaf */
  while (current && current->right != NULL)
    current = current->right;

  return current;
}

int ifdel = 0;
Node *deleteNode(Node *root, long long int x)
{

  if (root == NULL)
  {
    return NULL;
  }
  if (x < root->data)
  {
    root->left = deleteNode(root->left, x);
    // return root;
  }
  else if (x > root->data)
  {
    root->right = deleteNode(root->right, x);
    // return root;
  }
  // node to be deleted
  else
  {
    ifdel = 1;

    if (root->left == NULL)
    {
      Node *temp = root->right;
      free(root);
      ifdel = 1;
      return temp;
    }
    else if (root->right == NULL)
    {
      Node *temp = root->left;
      free(root);
      ifdel = 1;
      return temp;
    }
    Node *temp = maxValueNode(root->left);

    root->data = temp->data;

    root->left = deleteNode(root->left, temp->data);
  }

  return root;
}

void inorder(Node *root, long long int &i, int &res)
{
  if (root)
  {
    inorder(root->left, i, res);
    i--;
    if (i == 0)
      res = root->data;
    inorder(root->right, i, res);
  }
}
long long int ithSmallest(Node *root, long long int i)
{
  int res = 0;
  inorder(root, i, res);
  return res;
}

// height : 輸出此時 BST 的樹高

int getheight(Node *root)
{
  if (!root)
  {
    return 0;
  }
  int leftheight = 0;
  int rightheight = 0;
  Node *tmp = root;
  if (tmp->left)
  {
    leftheight = getheight(tmp->left);
  }
  if (tmp->right)
    rightheight = getheight(tmp->right);

  if (leftheight > rightheight)
  {
    leftheight += 1;
    return leftheight;
  }
  else if (leftheight <= rightheight)
  {
    rightheight += 1;
    return rightheight;
  }
}
// traversal : 輸出此 BST 的 level order traversal (每個輸出中間空格隔開)
void levelOrder(Node *root)
{
  if (!root)
    return;
  queue<Node *> q;
  q.push(root);
  int first = 1;
  while (!q.empty())
  {
    Node *temp = q.front();
    if (first)
    {
      cout << temp->data;
      first = 0;
    }
    else
    {
      cout << " " << temp->data;
    }
    q.pop();

    if (temp->left != NULL)
    {
      q.push(temp->left);
    }
    if (temp->right != NULL)
    {
      q.push(temp->right);
    }
  }
  cout << endl;
}
int main()
{
  Node *root = NULL;
  long long int x;
  while (1)
  {
    string str;
    getline(cin, str);
    string com = str.substr(0, str.find(" "));
    string xstr = str.substr(str.find(" ") + 1, str.length());
    int x = atoi(xstr.c_str());
    ifdel = 0;
    if (com == "traversal")
      break;
    else if (com == "height")
    {
      cout << getheight(root) << endl;
    }
    // insert
    else if (com == "insert")
    {
      root = insertNode(root, x);
      numNode++;
    }
    else if (com == "delete")
    {
      root = deleteNode(root, x);
      if (!ifdel)
      {
        cout << "cannot delete" << endl;
        numNode++;
      }
      numNode--;
    }
    else if (com == "search")
    {
      cout << ithSmallest(root, x) << endl;
    }
  }
  levelOrder(root);

  return 0;
}