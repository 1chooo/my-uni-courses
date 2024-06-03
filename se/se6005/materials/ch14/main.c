#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <libgen.h>
#include <stdint.h>
#include <errno.h>

#define OPTSTR "i:o:f:vh"
#define ERR_FOPEN_INPUT "Error opening input file"
#define ERR_FOPEN_OUTPUT "Error opening output file"
#define ERR_DO_THE_NEEDFUL "Error executing do_the_needful"

typedef struct {
    int verbose;
    uint32_t flags;
    FILE *input;
    FILE *output;
} option_t;

void usage(const char *progname, int opt) {
    fprintf(stderr, "Usage: %s [-i inputfile] [-o outputfile] [-f flags] [-v] [-h]\n", progname);
    exit(EXIT_FAILURE);
}

int do_the_needful(option_t *options) {
    // 這裡應該包含主要的業務邏輯
    // 這是一個示例，實際的實現可能會根據需求不同而不同
    char buffer[256];

    if (options->verbose) {
        printf("Verbose mode is on.\n");
        printf("Flags: 0x%08X\n", options->flags);
    }

    while (fgets(buffer, sizeof(buffer), options->input)) {
        if (options->verbose) {
            printf("Processing: %s", buffer);
        }
        fprintf(options->output, "%s", buffer);
    }

    return EXIT_SUCCESS;
}

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

    // 關閉文件
    if (options.input != stdin) {
        fclose(options.input);
    }
    if (options.output != stdout) {
        fclose(options.output);
    }

    return EXIT_SUCCESS;
}
