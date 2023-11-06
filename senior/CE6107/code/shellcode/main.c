#include<stdio.h>

int main(){
    setvbuf(stdout,0,2,0);

    char buf[100];
    printf( "Your input buffer address is %p\n" , buf );

    read( 0 , buf , 0x80 );

    return 0;
}