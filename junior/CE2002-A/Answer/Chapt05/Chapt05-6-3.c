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
  if (item.key > heap[position / 2].key)
  { /* new priority is higher than current priority */
    while (1)
      if ((position == 1) || (item.key <= heap[position / 2].key))
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
      if (child = heap[child].key)
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
    if ((position == 1) || (item.key <= heap[position / 2].key))
      break;
    else
    {
      heap[position] = heap[position / 2];
      position /= 2;
    }
  heap[position] = item;
  /* remove it from the heap, since it's now at the top */
  item = DeleteMaxHeap();
}

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