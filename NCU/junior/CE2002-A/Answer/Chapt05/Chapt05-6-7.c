#include <stdio.h>

#define TRUE 1
#define FALSE 0
#define MAX_ELEMENTS 100

typedef struct
{
  int key;
  /* other fields */
} element;
element heap[MAX_ELEMENTS];
int n = 0;
void InsertMinHeap(element);
element DeleteMinHeap();
void printHeap();
void HeapFull();
void HeapEmpty();
int searchHeap(int);
void changePriority(int);
void removePriority(int);
element topPriority();

int main()
{
  int choice, y, position;
  element x;

  printf("MIN Heap Operations \n\n");
  printf("1. Insert, 2. Delete, 3: Search 4. Top Priority 5. Change Priority 0. Quit:");
  scanf("%d", &choice);
  while (choice > 0)
  {
    switch (choice)
    {
    case 1:
      printf("Enter a number: ");
      scanf("%d", &x.key);
      printf("n = %d\n", n);
      InsertMinHeap(x);
      printHeap();
      break;
    case 2:
      x = DeleteMinHeap();
      printf("%d was deleted from the heap\n\n", x.key);
      printHeap();
      break;
    case 3:
      printf("Search for y: ");
      scanf("%d", &y);
      position = searchHeap(y);
      if (position)
        printf("%d was FOUND in position %d.\n", y, position);
      else
        printf("%d is not in the heap.\n", y);
      break;
    case 4:
      x = topPriority();
      printf("The top priority is: %d.\n", x.key);
      break;
    case 5:
      printf("Change Priority of: ");
      scanf("%d", &y);
      changePriority(y);
      printHeap();
      break;
    case 6:
      printf("Remove Priority: ");
      scanf("%d", &y);
      removePriority(y);
      printHeap();
    }
    printf("1. Insert, 2. Delete, 3: Search 4. Top Priority 5. Change Priority ");
    printf("6. Remove Priority 0. Quit:");
    scanf("%d", &choice);
  }
}

element topPriority() { return heap[1]; }

int searchHeap(int x)
{ /* search for x in the heap
    Time if 0(n) since heaps aren't
    organized for searching */
  int i;
  for (i = 1; i <= n; i++)
    if (heap[i].key == x)
      return i;
  return 0;
}

void printHeap()
{
  int i;
  for (i = 1; i <= n; i++)
    printf("[%d] = %d\n", i, heap[i].key);
}

void removePriority(int priority)
{ /*Remove an arbitrary item from the priority queue */
  int position, newPriority, parent, child;
  element item;
  position = searchHeap(priority);
  if (!(position))
  {
    printf("%d is not in the priority queue.\n", priority);
    return;
  }
  item = topPriority();
  item.key++;
  /* new priority is higher than top priority
     sift heap upward*/
  while (1)
    if ((position == 1) || (item.key >= heap[position / 2].key))
      break;
    else
    {
      heap[position] = heap[position / 2];
      position /= 2;
    }
  heap[position] = item;
  /* remove it from the heap, since it's now at the top */
  item = DeleteMinHeap();
}

void changePriority(int priority)
{ /*change priority of an item in the heap */
  int position, newPriority, parent, child;
  element item;
  position = searchHeap(priority);
  if (!(position))
  {
    printf("%d is not in the priority queue.\n", priority);
    return;
  }
  printf("New Priority: ");
  scanf("%d", &newPriority);
  item.key = newPriority;
  if (item.key < heap[position / 2].key)
  { /* new priority is lower than current priority */
    while (1)
      if ((position == 1) || (item.key >= heap[position / 2].key))
        /* terminate when the root is reached or the element
        is in its correct place */
        break;
      else
      {
        /* check the next lower level of the heap */
        heap[position] = heap[position / 2];
        position /= 2;
      }
    heap[position] = item;
  }
  else
  { /* new priority is lower, so go down the heap */
    parent = position;
    child = position * 2;
    while (child <= n)
    {
      if (child heap[child + 1].key)
        child++;
      if (item.key <= heap[child].key)
        /*correct position has been found */
        break;
      else
      {
        /* move to the next lower level */
        heap[parent] = heap[child];
        parent = child;
        child *= 2;
      }
    }
    heap[parent] = item;
  }
}

void HeapFull()
{ /* print an error message if the heap is full */
  printf("The heap is full, No insertion made \n");
}

void HeapEmpty()
{ /* print an error message if the heap is empty */
  printf("The heap is empty, No deletion made. \n");
}

void InsertMinHeap(element x)
{ /* insert x into the global max heap  [1..MAXELEMENTS-1]
    n (also global) is the present size of the heap */
  int i;
  if (n == MAX_ELEMENTS)
    HeapFull();
  else
  {
    i = ++n;
    while (1)
      if ((i == 1) || (x.key >= heap[i / 2].key))
        /* terminate when the root is reached or the element
        is in its correct place */
        break;
      else
      {
        /* check the next lower level of the heap */
        heap[i] = heap[i / 2];
        i /= 2;
      }
    heap[i] = x;
  }
}

element DeleteMinHeap()
{ /* delete element with the highest key from the heap */
  int parent, child;
  element x, temp;

  if (!n)
    HeapEmpty();
  else
  {
    /* save value of the element with the highest key */
    x = heap[1];
    temp = heap[n--]; /* use last element in heap to adjust heap */
    parent = 1;
    child = 2;
    while (child <= n)
    {
      if (child heap[child + 1].key)
        child++;
      if (temp.key <= heap[child].key)
        /*correct position has been found */
        break;
      else
      {
        /* move to the next lower level */
        heap[parent] = heap[child];
        parent = child;
        child *= 2;
      }
    }
    heap[parent] = temp;
    return x;
  }
}