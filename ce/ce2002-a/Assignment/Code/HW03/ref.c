#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct node
{
  int coef;
  int exp;
  struct node *next;
} node;

node *create_node(int coef, int exp)
{
  node *new_node = (node *)malloc(sizeof(node));
  new_node->coef = coef;
  new_node->exp = exp;
  new_node->next = NULL;
  return new_node;
}

void print_list(node *head)
{
  while (head != NULL)
  {
    if (head->coef != 0)
    {
      printf("%d %d ", head->coef, head->exp);
    }
    head = head->next;
  }
}

node *add_list(node *head1, node *head2)
{
  node *head3 = NULL;
  node *temp3 = NULL;
  while (head1 != NULL && head2 != NULL)
  {
    if (head1->exp > head2->exp)
    {
      if (head3 == NULL)
      {
        head3 = create_node(head1->coef, head1->exp);
        temp3 = head3;
      }
      else
      {
        temp3->next = create_node(head1->coef, head1->exp);
        temp3 = temp3->next;
      }
      head1 = head1->next;
    }
    else if (head1->exp < head2->exp)
    {
      if (head3 == NULL)
      {
        head3 = create_node(head2->coef, head2->exp);
        temp3 = head3;
      }
      else
      {
        temp3->next = create_node(head2->coef, head2->exp);
        temp3 = temp3->next;
      }
      head2 = head2->next;
    }
    else
    {
      if (head3 == NULL)
      {
        head3 = create_node(head1->coef + head2->coef, head1->exp);
        temp3 = head3;
      }
      else
      {
        temp3->next = create_node(head1->coef + head2->coef, head1->exp);
        temp3 = temp3->next;
      }
      head1 = head1->next;
      head2 = head2->next;
    }
  }
  while (head1 != NULL)
  {
    temp3->next = create_node(head1->coef, head1->exp);
    temp3 = temp3->next;
    head1 = head1->next;
  }
  while (head2 != NULL)
  {
    temp3->next = create_node(head2->coef, head2->exp);
    temp3 = temp3->next;
    head2 = head2->next;
  }
  return head3;
}

int main(void)
{
  int n1, n2;
  scanf("%d", &n1);
  node *head1 = NULL;
  node *temp = NULL;
  node *prev = NULL;
  for (int i = 0; i < n1; i++)
  {
    int coef, exp;
    scanf("%d %d", &coef, &exp);
    temp = create_node(coef, exp);
    if (i == 0)
    {
      head1 = temp;
      prev = temp;
    }
    else
    {
      prev->next = temp;
      prev = temp;
    }
  }

  scanf("%d", &n2);
  node *head2 = NULL;
  for (int i = 0; i < n2; i++)
  {
    int coef, exp;
    scanf("%d %d", &coef, &exp);
    temp = create_node(coef, exp);
    if (i == 0)
    {
      head2 = temp;
      prev = temp;
    }
    else
    {
      prev->next = temp;
      prev = temp;
    }
  }
  print_list(add_list(head1, head2));
  return 0;
}