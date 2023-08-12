// adding to the queue

void queue_full()
{ /* code to check for a full queue is in the
    addq() function */
  fprintf(stderr, "The queue is Full\n");
}

void addq(element item)
{ /* add an item to the global queue
      rear points to the current end of the queue */
  if (rear >= top - 1)
    queue_full();
  else
    memory[++rear] = item;
}

// delete from the queue

void queue_empty()
{ /* check for empty queue is in the deleteq() function */
  fprintf(stderr, "The queue is empty\n");
}

element deleteq()
{ /* remove element at the front of the queue */
  int i;
  element item = memory[0];
  if (!rear)
    queue_empty();
  else
  { /* shift downward */
    for (i = 1; i <= rear; i++)
      memory[i - 1] = memory[i];
    rear--;
    return item;
  }
}

// add to the stack
void add(element item)
{ /* add an item to the global stack
      top (also global) is the current top of the stack,
      MAX_SIZE is the maximum size */

  if (top <= rear + 1)
    StackFull();
  else
    memory[--top] = item;
}

// delete from the stack

void StackEmpty()
{
  printf("The stack is empty.  No item deleted \n");
}

element delete ()
{ /* remove top element from the stack and put it in item */
  if (top == MAX_SIZE)
    StackEmpty();
  else
    return memory[top++];
}