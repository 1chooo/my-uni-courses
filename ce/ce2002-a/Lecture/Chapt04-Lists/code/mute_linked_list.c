#include "stdio.h"
#include "stdlib.h"

typedef struct node {
  int data;
  struct node *next;
} Node;


int main(int argc, char *argv[]) {
  Node a, b, c;
  Node *ptr = &a;

  a.data = 12;
  a.next = &b;
  b.data = 30;
  b.next = &c;
  c.data = 64;
  c.next = NULL;

  while (ptr != NULL) {
    printf("address = %p, ", ptr);
    printf("data = %d ", ptr->data);
    printf("next = %p\n", ptr->next);

    ptr = ptr->next;
  }

  system("pause");

  return 0;
}