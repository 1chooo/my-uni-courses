void queue_full() { printf(“The queue is Full \n”); }
void queue_empty() { printf(“The queue is empty\n”); }
void addq(element item)
{ /* add an item to the global queue front and rear mark the two queue ends */
  if ((rear + 1 == front) || ((rear == MAX_QUEUE_SIZE - 1) && !front))
    queue_full();
  else
  {
    queue[rear] = item;
    rear = (rear + 1) % MAX_QUEUE_SIZE;
  }
}
element deleteq()
{ /*delete and element from the circular queue */
  int i;
  element temp;
  /* remove front element from the queue and put it in item */
  if (front == rear)
    queue_empty();
  else
  {
    temp = queue[front];
    front = (front + 1) % MAX_QUEUE_SIZE;
    return temp;
  }
}