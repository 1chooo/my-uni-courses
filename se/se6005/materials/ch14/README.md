# CH14 Process Automation - DEVOPS，Git Branch Model，and Tools


`gdb`

`*.gdb` (Marco)

`expect` command and how to automate shell like magic (gdb 不能輸入參數的解方)

> [!NOTE]
>
> 你知道 `main` program 要這樣寫嗎？

```c
/* main.c */

<...>

int main(int argc, char* argv[]) {
    int opt;
    option_t options = {0, 0x0, stdin, stdout};

    opterr = 0;

    while ((opt = getopt(argc, argv, OPTSTR)) != EOF) {
        switch (opt) {
            case 'i':
                if (!(options.input = fopen(optarg, "r"))) {
                    perror(ERR_FOPEN_INPUT);
                    exit(EXIT_FAILURE);
                    /* NOTREACHED */
                }
                break;
            case 'o':
                if (!(options.output = fopen(optarg, "w"))) {
                    perror(ERR_FOPEN_OUTPUT);
                    exit(EXIT_FAILURE);
                    /* NOTREACHED */
                }
                break;
            case 'f':
                options.flags = (uint32_t) strtoul(optarg, NULL, 16);
                break;
            case 'v':
                options.verbose += 1;
                break;
            case 'h':
            default:
                usage(basename(argv[0]), opt);
                /* NOTREACHED */
                break;
        }
    }

    if (do_the_needful(&options) != EXIT_SUCCESS) {
        perror(ERR_DO_THE_NEEDFUL);
        exit(EXIT_FAILURE);
        /* NOTREACHED */
    }
}
```

RPA (Robotic Process Automation) vs. Automation Script

- RPA 是取代人做的動作，而 Automation Script 是用 programming 思維來解決問題
