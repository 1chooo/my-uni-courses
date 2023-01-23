#include <stdio.h>
#include <stdlib.h>

struct node{
	int data;
	struct node *next;
};
typedef struct node Node;

int main(int argc, char *argv[])
{
  Node a,b,c;
  Node *ptr=&a; //宣告ptr，並將他只向節點a
  
  a.data=12;
  a.next=&b;
  b.data=30;
  b.next=&c;
  c.data=64;
  c.next=NULL;
  
  while(ptr!=NULL){
  	printf("address=%p, ",ptr); //印出節點的位址 
  	printf("data=%d ",ptr->data); //印出節點的資料 
  	printf("next=%p\n",ptr->next); //印出下一個節點位址 
  	ptr=ptr->next;  //將ptr指向下一個節點 
  } 
  
  system("PAUSE");	 
  return 0;
}