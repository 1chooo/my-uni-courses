#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define FALSE 0
#define TRUE 1
#define COMPARE(x, y) ((x) < (y) ? -1 : (x) == (y) ? 0 \
                                                   : 1)
typedef struct PolyNode *PolyPointer;
struct PolyNode
{
  float coef;
  int expon;
  PolyPointer link;
};
void attach(int, int, PolyPointer *);
PolyPointer GetNode();
void RetNode(PolyPointer);
void cerase(PolyPointer *);
PolyPointer av = NULL;
PolyPointer ReadPoly();
void PrintPoly(PolyPointer);
PolyPointer cpadd(PolyPointer, PolyPointer);
float evalPoly(float, PolyPointer);

int main()
{
  PolyPointer a, b, c;
  float x0;
  printf("Polynomial A: \n");
  a = ReadPoly();
  printf("Polynomial B: \n");
  b = ReadPoly();
  printf("Your polynomials are: \n");
  printf("Polynomial a: ");
  PrintPoly(a);
  printf("\nPolynomial b: ");
  PrintPoly(b);
  c = cpadd(a, b);
  printf("\n a+b = ");
  PrintPoly(c);
  printf("\n\nx0:");
  scanf("%f", &x0);
  printf("\nAt %f the polynomial is: %5.2f\n", x0, evalPoly(x0, a));
}

float evalPoly(float x0, PolyPointer ptr)
{ /*evaluate the polynomial */
  PolyPointer c;
  float result = 0;
  for (c = ptr->link; c != ptr; c = c->link)
  {
    result = result + c->coef * pow(x0, c->expon);
    printf("%f, %d\n", c->coef, c->expon);
  }
  return result;
}

PolyPointer ReadPoly()
{ /*read in the polynomial */
  PolyPointer node, c;
  float coefficient;
  int exponent;

  node = GetNode();
  node->coef = -1.0;
  node->expon = -1;
  node->link = node;
  printf("Enter an exponent < 0 to quit: ");
  printf("\nCoefficient, Exponent: ");
  scanf("%f,%d", &coefficient, &exponent);
  while (exponent >= 0)
  {
    c = GetNode();
    c->coef = coefficient;
    c->expon = exponent;
    c->link = node->link;
    node->link = c;
    printf("Coefficient, Exponent: ");
    scanf("%f,%d", &coefficient, &exponent);
  }
  return node;
}

void PrintPoly(PolyPointer ptr)
{ /*write out the polynomial */
  PolyPointer c;
  for (c = ptr->link; c != ptr; c = c->link)
    printf("<%5.2fx^%d>, ", c->coef, c->expon);
}

PolyPointer GetNode()
/* provide a node for use */
{
  PolyPointer node;
  if (!av)
    node = (PolyPointer)malloc(sizeof(struct PolyNode));
  else
  {
    node = av;
    av = av->link;
  }
  return node;
}

void attach(int coefficient, int exponent, PolyPointer *ptr)
{ /* create a new node with coef = coefficient and expon = exponent,
     attach it to the node pointed to by ptr.  ptr is updated to point
     to this new node */
  PolyPointer node;
  node = GetNode();
  node->coef = coefficient;
  node->expon = exponent;
  (*ptr)->link = node;
  *ptr = node;
}

PolyPointer cpadd(PolyPointer a, PolyPointer b)
{ /* polynomials a and b are singly linked lists, return
      a polynomial which is the sum of a and b */
  PolyPointer startA, c, lastC;
  int num, done = FALSE; /* jump out of switch and do loop */
  startA = a;            /* record start of a */
  a = a->link;           /* skip head node for a and b*/
  b = b->link;

  c = GetNode(); /* get a head node for c */
  c->expon = -1;
  c->coef = -1;
  lastC = c;
  do
  {
    switch (COMPARE(a->expon, b->expon))
    {
    case -1: /* a->expon < b->expon */
      attach(b->coef, b->expon, &lastC);
      b = b->link;
      break;
    case 0: /* a->expon = b->expon */
      if (startA == a)
        done = TRUE;
      else
      {
        num = a->coef + b->coef;
        if (num)
        {
          attach(num, a->expon, &lastC);
          a = a->link;
          b = b->link;
        }
      }
      break;
    case 1: /* a->expon > b->expon */
      attach(a->coef, a->expon, &lastC);
      a = a->link;
      break;
    }
  } while (!done);
  lastC->link = c;
  return c;
}