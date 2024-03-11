#include<stdio.h>

char code[6];

int main(){
    setvbuf(stdout,0,2,0);
    puts( "Give me your shellcode , I will execute it directly , but only 6 bytes :(");
    puts( "Six bytes is enough for excellent hacker :)" );

    int (*yuawn)() = (int(*)())code;

    read( 0 , code , 6 );

    puts("Your shellcode is running... 66666666");
    yuawn();

    return 0;
}