void queue_empty()
{ /* check for empty queue is in the deleteq() function */
  fprintf(stderr, “The queue is empty\n”);
}

void queue_full()
{ /* code to check for a full queue is in the  addq() function */
  fprintf(stderr, “The queue is Full\n”);
}

void addq(element item)
{ /* add an item to the global queue rear points to the current end of the queue */
  if (rear == MAX_QUEUE_SIZE - 1)
    queue_full();
  else
    queue[++rear] = item;
}

element deleteq()
{ /* remove element at the front of the queue */
  if (front == rear)
    queue_empty();
  else
    return queue[++front];
}