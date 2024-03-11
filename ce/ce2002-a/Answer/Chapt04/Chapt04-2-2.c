typedef struct listNode *listPointer;
typedef struct listNode {
  char data[4];
  listPointer link;
} ListNode;

listPointer ptr = NULL;

Call : if (search(ptr, key))
           printf("The key is in the list\n");
else printf("The key is not in the list\n");

listPointer search(listPointer ptr, int key)
{ /* determine if key is in the list */
     listPointer temp;
     for (temp = ptr; temp; temp = temp->link)
          if (temp->item.key == key)
               return temp;
     return NULL;
}