// delete number from the list

printf("Enter the number to delete: ");
scanf("%d", &num);
ptr = Deletelist(ptr, num, &found);
if (found)
  printf("The item was deleted from the list \n\n");
else
  printf("The item was not found in the list\n\n");

istpointer Deletelist(listpointer ptr, int searchNum, int *found)

/* search for an  element, delete it if it is in the list

   The pointer to the head of the list is returned in the function name,

   the value of found will be 1, if the entry was deleted, and 0

   otherwise */

{

  listpointer position, temp;

  position = search(ptr, searchNum, found);

  if (*found)
  {

    if (!position)
    {

      /* entry was  found at the head of the list, delete

      the current head pointer, and return the link field

      as the new pointer to the head of the list */

      temp = ptr->link;

      free(ptr);

      return temp;
    }

    else
    {

      /* entry was not at the head of the list, change the

      link pointers and free the storage */

      temp = position->link;

      position->link = temp->link;

      free(temp);

      return ptr;
    }
  }

  else

    /* item was not found in the list, return the pointer to

    the head of the list */

    return ptr;
}

// Modification of search that returns True/false

listpointer search(listpointer ptr, int searchNum, int *found)

{

  /* determine if searchNum is in the list, found will hold a value

     of TRUE (1) if  the item  was located, otherwise it will hold a value

     of FALSE (0).  The function name will hold the pointer to the entry prior

     to the one to be deleted.    */

  listpointer lead, trail;

  trail = NULL; /* entry prior to current one */

  lead = ptr; /* entry currently being examined */

  *found = FALSE;

  while (lead && !*found)

    if (lead->data == searchNum)

      *found = TRUE;

    else
    {

      trail = lead;

      lead = lead->link;
    }

  return trail;
}