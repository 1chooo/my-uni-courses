#include <assert.h>
#include <stdio.h>

#define SIZE 3

typedef enum {
    Comic,
    Novel,
    Magazine
} book_type;

typedef struct Book {
    book_type type;
} Book;

void print_book_type(Book *);

int main(void) {
    Book books[SIZE];
    books[0].type = Comic;
    books[1].type = Novel;
    books[2].type = Magazine;

    for (int i = 0; i < SIZE; i++) {
        print_book_type(&books[i]);
    }

    return 0;
}

void print_book_type(Book *book) {
    assert(book);

    switch (book->type) {
    case Comic:
        printf("Comic\n");
        break;
    case Novel:
        printf("Novel\n");
        break;
    case Magazine:
        printf("Maganize\n");
        break;
    }
}