# helloworld

```shell
$ nc 140.115.59.7 10000
$ chmod +x helloworld
$ objdump –M intel –d ./helloworld

$ file helloworld    
helloworld: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=dc55d847da53d1a7a2a57aad7c57d0d9ab3d5f69, for GNU/Linux 3.2.0, not stripped
```

Buffer 長度 32 

```c
int __fastcall main(int argc, const char **argv, const char **envp) {

    char v4[32]; // [rsp+0h] [rbp-20h] BYREF

    init(argc, argv, envp);
    puts("Are you new to ctf?");
    buts("Try to say helloworld in hacker's way!");
    gets(v4);
    return 0;
}
```