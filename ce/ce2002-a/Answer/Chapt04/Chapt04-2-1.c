void delete (listPointer *first, listPointer trail)
{ /* deletefrom the list, trail is the preceding node
 and *first is the front of the list */
  if (trail)
    trail->link = (*first)->link;
  else
    *first = (*first)->link;
  free(x);
}