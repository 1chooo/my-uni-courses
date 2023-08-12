Call : 
if (searchList(x, ptr))
  printf("%d is in the list.\n", x);
else 
  printf("%d is Not in the list.\n", x);

listPointer searchList(int x, listPointer ptr)
{ /* print out the contents of the list */
  listPointer temp = ptr;
  do
  {
    if (temp->data == x)
      return temp;
    temp = temp->link;
  } while (temp != ptr);
  return NULL;
}