#include "stdio.h"
#include "stdlib.h"
#include "string.h"

// Declariations

#define MAX_SIZE 6

typedef struct
{

  int key;
} element;

element deque[MAX_SIZE]; /* global queue declaration */

int rear = -1;

void deque_empty()

{
  fprintf(stderr, "The deque is empty\n");
}

void deque_full()

{
  fprintf(stderr, "The deque is Full\n");
}

// Adding to the front

void addFront(element item)

{ /* add an item to the front of the dequeu */

  int i;

  if (rear == MAX_SIZE - 1)

    deque_full();

  else
  {

    rear++;

    if (rear > 0) /* shift if deque isn't empty */

      for (i = rear; i > 0; i--)

        deque[i] = deque[i - 1];

    deque[0] = item;
  }
}

// Adding to the rear

void addRear(element item)

{ /* add an item to the high end of the global deque

      rear points to the current end of the deque */

  if (rear == MAX_SIZE - 1)

    deque_full();

  else

    deque[++rear] = item;
}

// Deleting from the front

element deleteFront()

{ /* remove element at the front of the deque */

  int i;

  if (rear < 0)

    deque_empty();

  else
  { /* shift downward */

    element item = deque[0];

    for (i = 1; i <= rear; i++)

      deque[i - 1] = deque[i];

    rear--;

    return item;
  }
}

// Deleting from the rear

element deleteRear()

{ /* remove element at the high end of the deque */

  if (rear < 0)

    deque_empty();

  else

    return deque[rear--];
}

// Driver

int main(void)
{

  printf("1. Add to front, 2. Delete front, 3. Add to  rear, 4. Delete rear, 0. Quit: ");

  scanf("%d", &choice);

  while (choice > 0)
  {

    switch (choice)
    {

    case 1:
      printf("Enter the number to insert: ");

      scanf("%d", &item.key);

      addFront(item);

      break;

    case 2:
      item = deleteFront();

      if (rear >= 0)

        printf("%d was deleted from the queue.\n\n", item.key);

      break;

    case 3:
      printf("Enter the number to insert: ");

      scanf("%d", &item.key);

      addRear(item);

      break;

    case 4:
      item = deleteRear();

      if (rear >= 0)

        printf("%d was deleted from the stack \n\n", item.key);

      break;
    }
  }
}