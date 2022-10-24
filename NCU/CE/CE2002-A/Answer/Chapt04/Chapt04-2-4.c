Call : 
  printf("The list contains %4d elements:\n\n", length(ptr));

int length(list_pointer ptr)
{ /* find the length of the list */
  list_pointer temp;
  int size;
  size = 0;
  for (temp = ptr; temp; temp = temp->link)
    size++;
  return size;
}