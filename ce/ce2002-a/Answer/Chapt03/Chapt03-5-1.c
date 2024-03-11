#include "stdio.h"
#include "stdlib.h"


// Stack declarations
#define MAX_SIZE 6
typedef struct
{
  int key;
} element;

element memory[MAX_SIZE]; /* global queue declaration */
int top[2];
top[0] = -1;
top[1] = MAX_SIZE;

CALLS : printf("1. Insert stack 0, 2.Delete stack 0, 3. Insert Stack 1, 4. Delete Stack 1, 0. Quit: ");
scanf("%d", &choice);
while (choice > 0)
{
  switch (choice)
  {
  case 1:
    printf("Insert in stack 0: ");
    scanf("%d", &item.key);
    add(0, item);
    break;
  case 2:
    item = delete (0);
    if (top[0] >= 0)
      printf("%d was deleted from the stack 0.\n\n", item.key);
    break;
  case 3:
    printf("Enter the number to insert: ");
    scanf("%d", &item.key);
    add(1, item);
    break;
  case 4:
    item = delete (1);
    if (top[1] < MAX_SIZE)
      printf("%d was deleted from the stack 1 \n\n", item.key);
    break;
  }
}


// adding to stack
void StackFull()
{
  printf("The stack is full.  No item added \n");
}


void add(int topNo, element item)
{ /* add an item to the global stack
      top (also global) is the current top of the stack,
      MAX_SIZE is the maximum size */

  if (top[0] + 1 >= top[1])
    StackFull();
  else
  {
    if (!topNo)
      memory[++top[0]] = item;
    else
      memory[--top[1]] = item;
  }
}


// delete from stack.
void StackEmpty()
{
  printf("The stack is empty.  No item deleted \n");
}
element delete (int topNo)
{ /* remove top element from the stack and put it in item */
  if (!topNo)
  {
    if (top[0] < 0)
      StackEmpty();
    return memory[top[0]--];
  }
  else
  { /*second stack */
    if (top[1] == MAX_SIZE)
      StackEmpty();
    return memory[top[1]++];
  }
}