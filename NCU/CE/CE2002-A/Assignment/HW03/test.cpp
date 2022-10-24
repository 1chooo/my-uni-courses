#include <iostream>
#include <cstring>

using namespace std;

typedef struct Polynomial
{
  int con;
  int pow;
  Polynomial *next;
} Node;

// void add_Node(Polynomial *cu, int con, int pow)
//{
//	while(true)
//	{
//		if(cu->next == NULL || cu == NULL)
//		{
//			cu->next = new Polynomial;
//			cu = cu->next;
//			cu->con = con;
//			cu->pow = pow;
//			cu->next = NULL;
//			break;
//		}
//		else
//		{
//			cu= cu->next;
//		}
//	}
// }
// void add_Node(Polynomial *head, Polynomial *cur, int m, int n)
//{
//	Node* newNode = new Node();
//	newNode->con = m;
//	newNode->pow = n;
//	newNode->next = NULL;
//	if(head == NULL)
//	{
//		head = newNode;
//		cur = newNode;
//		return;
//	}
//	if(cur ->next == NULL)
//	{
//		Node* temp = cur;
//		temp ->next = newNode;
//		cur = newNode;
//		return;
//	}
//
// }
Polynomial *CreateNode(Polynomial *cu, int con, int pow)
{
  while (true)
  {
    if (cu->next == NULL)
    {
      cu->next = new Polynomial;
      cu = cu->next;
      cu->con = con;
      cu->pow = pow;
      cu->next = NULL;
      return cu;
      break;
    }
    else
    {
      cu = cu->next;
    }
  }
}
void check_Node(Polynomial *cu)
{
  cu = cu->next;
  while (true)
  {

    if (cu == NULL)
      return;

    {
      if (cu->con == 0)
        cu = cu->next;

      else
      {
        cout << cu->con << " " << cu->pow << " ";
        cu = cu->next;
      }
    }
  }
}

void add_up_Node(Polynomial *one, Polynomial *two, Polynomial *three)
{
  one = one->next;
  two = two->next;

  while (true)
  {
    if (one == NULL and two == NULL)
    {
      three->next = NULL;
      break;
    }

    three->next = new Polynomial;
    three = three->next;

    if (one == NULL)
    {
      three->con = two->con;
      three->pow = two->pow;
      two = two->next;
    }
    else if (two == NULL)
    {
      three->con = one->con;
      three->pow = one->pow;
      one = one->next;
    }
    else
    {
      if (one->pow > two->pow)
      {
        three->con = one->con;
        three->pow = one->pow;
        one = one->next;
      }
      else if (one->pow == two->pow)
      {
        three->con = (one->con + two->con);
        three->pow = one->pow;

        one = one->next;
        two = two->next;
      }
      else if (one->pow < two->pow)
      {
        three->con = two->con;
        three->pow = two->pow;
        two = two->next;
      }
    }
  }
}

Polynomial *A = NULL, *B = NULL, *C = NULL, *curA = NULL, *curB = NULL, *curC = NULL;

// int main()
//{
////	POL *A,*B,*C;
//
////	A = new Polynomial;
////	B = new Polynomial;
////	C = new Polynomial;
////
////	A->next = NULL;
////	B->next = NULL;
////	C->next = NULL;
//
//	int num1, num2;
//	cin>>num1;
//	for(int i=0; i<num1; i++)
//	{
//		int m, n;
//		cin>>m>>n;
//		CreateNode(A, curA,  m, n);
//	}
//	cin>>num2;
//	for(int i=0; i<num2; i++)
//	{
//		int m, n;
//		cin>>m>>n;
//		CreateNode(B, curB, m, n);
//	}
//	check_Node(A);
//	cout<<endl;
//	check_Node(B);
//	cout<<endl;
//
//	add_up_Node(A, B, C);
//
//
//	check_Node(C);
//
//	return 0;
//}
int main()
{
  Polynomial *A, *B, *C, *pEnd;

  A = new Polynomial;
  B = new Polynomial;
  C = new Polynomial;

  A->next = NULL;
  B->next = NULL;
  C->next = NULL;

  int num1, num2;
  cin >> num1;

  pEnd = A;
  for (int i = 0; i < num1; i++)
  {
    int m, n;
    cin >> m >> n;
    pEnd = CreateNode(pEnd, m, n);
  }
  cin >> num2;

  pEnd = B;
  for (int i = 0; i < num2; i++)
  {
    int m, n;
    cin >> m >> n;
    pEnd = CreateNode(pEnd, m, n);
  }

  add_up_Node(A, B, C);

  check_Node(C);

  return 0;
}