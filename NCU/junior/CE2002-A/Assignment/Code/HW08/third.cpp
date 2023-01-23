#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;
vector<string> output;
class BST;
class TreeNode
{
  // private:

public:
  TreeNode *leftchild;
  TreeNode *rightchild;
  TreeNode *parent;
  long long int key;

  TreeNode() : leftchild(0), rightchild(0), parent(0), key(0){};
  TreeNode(long long int a) : leftchild(0), rightchild(0), parent(0), key(a){};

  long long int GetKey() { return key; } // 為了在main()要能夠檢視node是否正確

  // 其餘情況, 因為class BST是class TreeNode的friend class
  // 在class BST的member function中, 可以直接存取class TreeNode的private data

  friend class BST; // 放在 private 或 public 都可以
};

class BST
{
  // private:

public:
  TreeNode *root;
  TreeNode *Leftmost(TreeNode *current);
  TreeNode *Successor(TreeNode *current);
  TreeNode *Rightmost(TreeNode *current);
  TreeNode *Predecessor(TreeNode *current);

  BST() : root(0){};

  TreeNode *Search(long long int key);

  void InsertBST(long long int key);

  void InorderPrint();

  void Levelorder();

  void DeleteBST(long long int key);

  long long int maxDepth(TreeNode *node);

  TreeNode *get_root();
};

TreeNode *BST::Search(long long int KEY)
{

  TreeNode *current = root; // 將curent指向root作為traversal起點
  if (current == NULL)
  {
    return current;
  }
  while (current != NULL && KEY != current->key)
  { // 兩種情況跳出迴圈：
    // 1.沒找到 2.有找到
    if (KEY < current->key)
    {
      current = current->leftchild; // 向左走
    }
    else
    {
      current = current->rightchild; // 向右走
    }
  }
  return current;
}
TreeNode *BST::get_root()
{
  TreeNode *r = root;
  return r;
}
void BST::InsertBST(long long int key)
{

  TreeNode *y = 0; // 準新手爸媽
  TreeNode *x = 0; // 哨兵
  TreeNode *insert_node = new TreeNode(key);

  x = root;
  while (x != NULL)
  { // 在while中, 以如同Search()的方式尋找適當的位置
    y = x;
    if (insert_node->key < x->key)
    {
      x = x->leftchild;
    }
    else
    {
      x = x->rightchild;
    }
  }                        // 跳出迴圈後, x即為NULL
                           // y即為insert_node的parent
  insert_node->parent = y; // 將insert_node的parent polong long inter指向y

  if (y == NULL)
  { // 下面一組if-else, 把insert_node接上BST
    this->root = insert_node;
  }
  else if (insert_node->key < y->key)
  {
    y->leftchild = insert_node;
  }
  else
  {
    y->rightchild = insert_node;
  }
}
TreeNode *BST::Rightmost(TreeNode *current)
{

  while (current->rightchild != NULL)
  {
    current = current->rightchild;
  }
  return current;
}
TreeNode *BST::Predecessor(TreeNode *current)
{
  if (current->leftchild != NULL)
  {
    return Rightmost(current->leftchild);
  }

  TreeNode *new_node = current->parent;

  while (new_node != NULL && current == new_node->leftchild)
  {
    current = new_node;
    new_node = new_node->parent;
  }
  return new_node;
}
TreeNode *BST::Leftmost(TreeNode *current)
{

  while (current->leftchild != NULL)
  {
    current = current->leftchild;
  }
  return current;
}
TreeNode *BST::Successor(TreeNode *current)
{

  if (current->rightchild != NULL)
  {
    return Leftmost(current->rightchild);
  }

  TreeNode *new_node = current->parent;

  while (new_node != NULL && current == new_node->rightchild)
  {
    current = new_node;
    new_node = new_node->parent;
  }

  return new_node;
}
vector<long long int> v;
void BST::InorderPrint()
{
  TreeNode *current = new TreeNode;
  current = Leftmost(root);
  v.clear();
  while (current)
  {
    v.push_back(current->key);
    //        cout <<  "(" << current->key << ")" << " ";
    current = Successor(current);
  }
}
// vector<int> level_output;
void BST::Levelorder()
{
  if (root == NULL)
  {
    return;
  }
  std::queue<TreeNode *> q;
  q.push(this->root); // 把root作為level-order traversal之起點
                      // 推進queue中
  while (!q.empty())
  { // 若queue不是空的, 表示還有node沒有visiting

    TreeNode *current = q.front(); // 取出先進入queue的node
    q.pop();
    cout << current->key << " ";
    //    	level_output.push_back(current->key);

    if (current->leftchild != NULL)
    { // 若leftchild有資料, 將其推進queue
      q.push(current->leftchild);
    }
    if (current->rightchild != NULL)
    { // 若rightchild有資料, 將其推進queue
      q.push(current->rightchild);
    }
  }
}
void BST::DeleteBST(long long int KEY)
{ // 要刪除具有KEY的node

  TreeNode *delete_node = Search(KEY); // 先確認BST中是否有具有KEY的node

  if (delete_node == NULL)
  {
    //        cout << "cannot delete"<<endl;
    output.push_back("cannot delete");
    return;
  }

  TreeNode *y = 0; // 真正要被刪除並釋放記憶體的node
  TreeNode *x = 0; // 要被刪除的node的"child"

  if (delete_node->leftchild == NULL || delete_node->rightchild == NULL)
  {
    y = delete_node;
  }
  else
  {
    y = Predecessor(delete_node); // 將y設成delete_node的Successor
  }                               // 經過這組if-else, y調整成至多只有一個child
                                  // 全部調整成case1或case2來處理
  if (y->leftchild != NULL)
  {
    x = y->leftchild; // 將x設成y的child, 可能是有效記憶體,
  }                   // 也有可能是NULL
  else
  {
    x = y->rightchild;
  }
  if (x != NULL)
  { // 在y被刪除之前, 這個步驟把x接回BST
    x->parent = y->parent;
  }
  // 接著再把要被釋放記憶體的node之"parent"指向新的child
  if (y->parent == NULL)
  { // 若刪除的是原先的root, 就把x當成新的root
    this->root = x;
  }
  else if (y == y->parent->leftchild)
  {                           // 若y原本是其parent之left child
    y->parent->leftchild = x; // 便把x皆在y的parent的left child, 取代y
  }
  else
  {                            // 若y原本是其parent之right child
    y->parent->rightchild = x; // 便把x皆在y的parent的right child, 取代y
  }
  // 針對case3
  if (y != delete_node)
  {                            // 若y是delete_node的替身, 最後要再將y的資料
    delete_node->key = y->key; // 放回delete_node的記憶體位置, 並將y的記憶體位置釋放
  }
  //    delete y;                               // 將y的記憶體位置釋放
  //    y = 0;
}
long long int BST::maxDepth(TreeNode *node)
{
  if (node == NULL)
    return 0;
  else
  {
    /* compute the depth of each subtree */
    long long int lDepth = BST::maxDepth(node->leftchild);
    long long int rDepth = BST::maxDepth(node->rightchild);

    /* use the larger one */
    if (lDepth > rDepth)
      return (lDepth + 1);
    else
      return (rDepth + 1);
  }
}
// when root = NULL
// problem:
// root->key
// Search
int main()
{

  BST T;
  //    TreeNode *root = T.get_root();
  //    cout<<"key"<<root->key<<" child:"<<root->rightchild;
  string s;
  string i;
  long long int a;
  //    cin>>a;
  //    TreeNode *tmp;
  //    T.DeleteBST(a);

  cin >> s;
  while (s != "traversal") //(cin>>s)  //cin.get() != '\n'
  {
    if (s == "insert")
    {
      cin >> a;
      T.InsertBST(a);
    }
    else if (s == "delete")
    {
      cin >> a;
      T.DeleteBST(a);
    }
    else if (s == "search")
    {
      cin >> a;
      T.InorderPrint();
      output.push_back(to_string(v[a - 1]));
    }
    else if (s == "height")
    {
      TreeNode *root = T.get_root();

      output.push_back(to_string(T.maxDepth(root)));
    }

    cin >> s;
  }

  //    for(long long int i=500;i<1000;i++) T.InsertBST(i);
  //    for(long long int i=500;i<600;i++) T.DeleteBST(i);
  //    for(long long int i=1;i<100;i++)
  //    {
  //        T.InorderPrint();
  //        output.push_back(to_string(v[i-1]));
  //    }
  //    for(long long int i=0;i<1;i++)
  //    {
  //        TreeNode *root = T.get_root();
  //        output.push_back(to_string(T.maxDepth(root)));
  //    }
  for (int i = 0; i < output.size(); i++)
  {
    cout << output[i] << endl;
  }
  T.Levelorder();

  return 0;
}

// insert 6
// insert 2
// insert -1
// insert 3
// insert 0
// insert 9
// insert 7
// insert 12
// delete 2
// traversal