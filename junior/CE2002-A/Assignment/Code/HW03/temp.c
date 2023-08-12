#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1
#define COMPARE(x,y) ((x) < (y) ? -1 : (x) == (y) ? 0 : 1)

typedef struct polynode *polypointer;

struct polynode
{
  int coef;
  int expon;
  polypointer link;
};

polypointer readpoly();
polypointer padd(polypointer, polypointer);
polypointer cpadd(polypointer, polypointer);

void attach(int coefficient, int exponent, polypointer *ptr);
void printpoly(polypointer node);

int main()
{
  polypointer a, b, c;
  a = readpoly();
  // printpoly(a);
  b = readpoly();
  // printpoly(b);
  c = padd(a, b);
  printpoly(c);
  return 0;
}

void attach(int coefficient, int exponent, polypointer *ptr)
{
  polypointer node;
  node = (polypointer)malloc(sizeof(struct polynode));
  node->coef = coefficient;
  node->expon = exponent;
  node->link = NULL;
  (*ptr)->link = node;
  *ptr = node;
}

polypointer readpoly()
{
  polypointer node, rear, c;
  int coefficient, exponent, num;
  scanf("%d", &num);
  node = (polypointer)malloc(sizeof(struct polynode));
  node->link = NULL;
  rear = node;
  while (num--)
  {
    scanf("%d %d", &coefficient, &exponent);
    attach(coefficient, exponent, &rear);
  }
  c = node;
  node = node->link;
  free(c);
  return node;
}

void printpoly(polypointer node)
{
  int flag = 0;
  if (!node)
  {
    // printf("0 0\n");
    return;
  }
  while (node)
  {
    if (!flag)
    {
      flag = 1;
    }
    else
    {
      if (flag > 1)
      {
        printf(" ");
      }
      flag = 2;
      if (node->coef == 0)
      {
        flag = 1;
      }
      if (node->coef != 0)
      {
        printf("%d %d", node->coef, node->expon);
      }
      node = node->link;
    }
  }
}

polypointer padd(polypointer a, polypointer b)
{
  polypointer front, rear, temp;
  int sum;
  rear = (polypointer)malloc(sizeof(struct polynode));
  front = rear;
  while (a && b)
  {
    if (a->expon == b->expon)
    {
      sum = a->coef + b->coef;
      if (sum)
      {
        attach(sum, a->expon, &rear);
        a = a->link;
        b = b->link;
      }
      else
      {
        a = a->link;
        b = b->link;
      }
    }
    else if (a->expon > b->expon)
    {
      attach(a->coef, a->expon, &rear);
      a = a->link;
    }
    else
    {
      attach(b->coef, b->expon, &rear);
      b = b->link;
    }
  }

  while (a)
  {
    attach(a->coef, a->expon, &rear);
    a = a->link;
  }
  while (b)
  {
    attach(b->coef, b->expon, &rear);
    b = b->link;
  }
  rear->link = NULL;
  temp = front;
  front = front->link;
  free(temp);
  return front;
}

polypointer cpadd(polypointer a, polypointer b)
{
  polypointer starta, c, lastc;
  int sum, done = FALSE;
  starta = a;
  a = a->link;
  b = b->link;
  c = getnode();
  c->expon = -1;
  lastc = c;
  do
  {
    switch (COMPARE(a->expon, b->expon))
    {
    case -1:
      attach(b->coef, b->expon, &lastc);
      b = b->link;
      break;
    case 0:
      if (starta == a)
      {
        done = TRUE;
      }
      else
      {
        sum = a->coef + b->coef;

        if (sum)
        {
          attach(sum, a->expon, &lastc);
          a = a->link;
          b = b->link;
        }
      }
      break;
    case 1:
      attach(a->coef, a->expon, &lastc);
      a = a->link;
    }
  } while (!done);
  lastc->link = c;
  return c;
}