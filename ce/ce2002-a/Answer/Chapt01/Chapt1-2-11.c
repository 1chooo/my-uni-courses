
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define Tower1 1
#define Tower2 2
#define Tower3 3
void towers_of_hanoi(int, int, int, int);

int main(){
	int n_disks;
	printf("Number of disks: "); 
	scanf("%d", &n_disks);
	printf("Disk, source, and destination towers listed below\n");
    printf("%12s%10s%15s\n", "Disk No", "Source","Destination");
    towers_of_hanoi(n_disks,Tower1,Tower3,Tower2);
}

void towers_of_hanoi(int n_disks, int source, int dest, int spare){
  if (n_disks == 1 ) 
    printf("%10d%10d%10d\n", n_disks, source, dest);
   else {
      /*move a disk from source to spare*/
      towers_of_hanoi(n_disks-1,source,spare,dest);
	  printf("%10d%10d%10d\n", n_disks, source, dest);
	  /*move a disk from spare to destination tower*/
      towers_of_hanoi(n_disks-1,spare,dest,source);
  }
}