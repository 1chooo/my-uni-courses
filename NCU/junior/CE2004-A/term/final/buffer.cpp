#include <iostream>

#define BufferSize 60

char* poi = "The summer break is around the corner.";
char sentence[BufferSize];

int ppp(char* s, char* d, unsigned len) {
    unsigned i;
    for (i = 0; i < len; ++i) {
        *(d + i) = *(s + i);
    }
    return i;
}

void goo(char* s, char* d, int length) {
    if (length < BufferSize) {
        ppp(s, d, length);
    }
}

int main() {
    goo(poi, sentence, 20);

    // 輸出結果
    std::cout << "Result: " << sentence << std::endl;

    return 0;
}
