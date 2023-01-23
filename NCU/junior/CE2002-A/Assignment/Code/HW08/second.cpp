#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <sstream>
#define Max_Size 1000

struct bst
{
  int data;
  bst *left;
  bst *right;

  bst(int val)
      : data(val), left(nullptr), right(nullptr) {}
};

void Insert(bst *&root, int key)
{
  bst *node = new bst(key);
  if (!root)
  {
    root = node;
    return;
  }
  bst *prev = nullptr;
  bst *temp = root;
  while (temp)
  {
    if (temp->data > key)
    {
      prev = temp;
      temp = temp->left; // left_tree < root < right_tree
    }
    else if (temp->data < key)
    {
      prev = temp;
      temp = temp->right; // left_tree < root < right_tree
    }
  }
  if (prev->data > key)
    prev->left = node;
  else
    prev->right = node;
}

void Level_Order(bst *root)
{
  if (!root)
  {
    // std::cout << "The binary search tree is EMPTY!";
    return;
  }
  std::queue<bst *> q_bstptr;
  q_bstptr.push(root);
  while (!q_bstptr.empty())
  {
    bst *current = q_bstptr.front();
    q_bstptr.pop();
    std::cout << current->data << ' ';

    if (current->left)
      q_bstptr.push(current->left);
    if (current->right)
      q_bstptr.push(current->right);
  }
  std::cout << '\n';
}

int Height(bst *root)
{
  int height = 0;
  if (!root)
    return height;
  std::queue<bst *> q_bstptr;
  q_bstptr.push(root);
  while (!q_bstptr.empty())
  {
    int size = q_bstptr.size();
    for (int i = 0; i < size; i++)
    {
      bst *temp = q_bstptr.front();
      q_bstptr.pop();
      if (temp->left)
        q_bstptr.push(temp->left);
      if (temp->right)
        q_bstptr.push(temp->right);
    }
    height++;
  }
  return height;
}

bst *GetMaximumKey(bst *current)
{
  while (current->right)
  {
    current = current->right;
  }
  return current;
}

bst *GetMinimumKey(bst *current)
{
  while (current->left)
  {
    current = current->left;
  }
  return current;
}

bst *Search(bst *&current, int key, bst *&prev)
{
  while (current && key != current->data)
  {
    prev = current;
    if (key < current->data)
      current = current->left;
    else if (key > current->data)
      current = current->right;
  }
  return current;
}

void Delete(bst *&root, int key)
{
  bst *prev = nullptr;
  bst *current = root;
  Search(current, key, prev);
  if (current == nullptr)
  {
    std::cout << "cannot delete\n"; // current is the delete_node
    return;
  }

  // current (delete_node) is a leaf node
  if (current->left == nullptr && current->right == nullptr)
  {

    if (current != root)
    {
      if (prev->left == current)
        prev->left = nullptr;
      else
        prev->right = nullptr;
    }
    else
      root = nullptr;

    delete (current);
  }

  // current (delete_node) has two child
  else if (current->left && current->right)
  {
    bst *predecessor = GetMaximumKey(current->left);

    int val = predecessor->data;
    Delete(root, val);
    current->data = val;
  }

  // current (delete_node) has only one child
  else
  {
    bst *child;
    if (current->left)
      child = current->left;
    else
      child = current->right;

    if (current != root)
    {

      if (current == prev->left)
        prev->left = child;
      else
        prev->right = child;
    }
    else
      root = child;

    delete (current);
  }
}

std::vector<int> Inorder(bst *root, std::vector<int> &dataset)
{
  if (root != nullptr)
  {
    Inorder(root->left, dataset);
    dataset.push_back(root->data);
    Inorder(root->right, dataset);
  }
  return dataset;
}

void find_nth_minimum(bst *root, int n)
{
  if (!root)
  {
    return;
  }
  std::vector<int> dataset;
  dataset = Inorder(root, dataset);
  int nth_minimum_val = dataset[n - 1];
  std::cout << nth_minimum_val << '\n';
}

int main()
{
  bst *root = nullptr;
  std::vector<int> dataset;
  dataset.reserve(Max_Size);
  std::string line, input;
  std::stringstream ss;
  int num;
  while (std::getline(std::cin, line))
  {
    if (line != "traversal")
    {
      ss << line;
      ss >> input;

      if (input == "insert")
      {
        ss >> num;
        Insert(root, num);
      }
      else if (input == "delete")
      {
        ss >> num;
        Delete(root, num);
      }
      else if (input == "search")
      {
        ss >> num;
        find_nth_minimum(root, num);
      }
      else if (input == "height")
      {
        std::cout << Height(root) << '\n';
      }

      ss.str("");
      ss.clear();
    }
    else
    {
      Level_Order(root);
      ss.str("");
      ss.clear();
      break;
    }
  }
  return 0;
}