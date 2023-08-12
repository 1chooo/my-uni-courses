// how do I add the expression tree?
class ExpressionTree
{
  struct Node
  {
    std::string data;

    Node *leftChild, *rightChild;
    Node *parent; // +

    Node(std::string d, Node *p) : data(d), leftChild(NULL), rightChild(NULL), parent(p) {}
  } * root;
  uint tsize;

public:
  ExpressionTree() : root(NULL), tsize(0) {}
  Node *treeRoot() { return root; }
  void insert(std::string s);
};

void insert(std::string s)
{
  if (root == NULL)
  {
    root = new Node(s, NULL);
    ++tsize;
  }
  else
  {
    Node *current = root;
    while (true)
    {
      if (is_operator(current - &gt; data))
      {
        if (current - &gt; leftChild == NULL)
        {
          current - &gt;
          leftChild = new Node(s, current);
          ++tsize;
          return;
        }
        else if (current - &gt; rightChild == NULL)
        {
          current - &gt;
          rightChild = new Node(s, current);
          ++tsize;
          return;
        }
        else
        {
          if (is_operator(current - &gt; leftChild - &gt; data))
          {
            current = current - &gt;
            leftChild;
            continue;
          }
          else if (is_operator(current - &gt; rightChild - &gt; data))
          {
            current = current - &gt;
            rightChild;
            continue;
          }
          else
          {
            current = current - &gt;
            parent - &gt;
            rightChild; // +
            continue;
          }
        }
      }
      else
      {
        std::cout &lt;
        &lt;
        "Error: only nodes who hold operators " & lt;
        &lt;
        "can have children." & lt;
        &lt;
        std::endl;
        return;
      }
    }
  }
}

vector<long long> num;
vector<char> expression;

typedef struct node
{
  char data;
  struct node *leftChild, *rightChild;
} Node;

Node *createTreeNode(int);
Node *createTree(char[], int, int);

void inorder(Node *);
void preorder(Node *);
void postorder(Node *);

long long turnPostorder(long long, char *);

for (int i = 0; i < arr.size(); i++)
{
  cout << arr.at(i) << " ";
}
cout << endl;

long long operand1, operand2, result;
char opr;
for (int i = 0; i < arr.size(); i++)
{
  if (arr.at(i) != 'j')
  {
    if (arr.at(i) <= '9' && arr.at(i) >= '0')
    {
      num.push_back(arr.at(i) - '0');
    }

    expression.push_back(arr.at(i));

    operand2 = num.at(num.size() - 1);
    operand1 = num.at(num.size() - 2);
    num.pop_back();
    num.pop_back();
    opr = expression.at(0);
    expression.pop_back();
    // opr = expression.pop_back();

    switch (opr)
    {
    case '+':
      result = operand1 + operand2;
      break;
    case '-':
      result = operand1 - operand2;
    case '*':
      result = operand1 * operand2;
    case '/':
      result = operand1 / operand2;
    default:
      break;
    }

    num.push_back(result);
  }
}

// Node* root = createTree(stack, 0, nums);

// postorder(root);

Node *createTreeNode(char data)
{
  Node *treeNode = (Node *)malloc(sizeof(Node));

  treeNode->data = data;
  treeNode->leftChild = NULL;
  treeNode->rightChild = NULL;

  return treeNode;
}

Node *createTree(char stack[], int index, int num)
{
  Node *root = NULL;

  if (index < num)
  {
    root = createTreeNode(stack[index]);
    root->leftChild = createTree(stack, 2 * index + 1, num);
    root->rightChild = createTree(stack, 2 * index + 2, num);
  }

  return root;
}

void postorder(Node *ptr)
{ /* postorder tree traversal */
  if (ptr)
  {
    postorder(ptr->leftChild);
    postorder(ptr->rightChild);
    // cout << ptr->data << " ";
    arr.push_back(ptr->data);
  }

  return;
}