#include <iostream>

#define SIZE 3


class Book {
public:
    virtual void print_book_type() = 0;
};

class ComicBook : public Book {
public:
    void print_book_type() {
        std::cout << "Comic" << std::endl;
    }
};

class NovelBook : public Book {
public:
    void print_book_type() {
        std::cout << "Novel" << std::endl;
    }
};

class MagazineBook : public Book {
public:
    void print_book_type() {
        std::cout << "Magazine" << std::endl;
    }
};

int main() {
    Book* books[SIZE];

    ComicBook comicBook;
    NovelBook novelBook;
    MagazineBook magazineBook;

    books[0] = &comicBook;
    books[1] = &novelBook;
    books[2] = &magazineBook;

    for (int i = 0; i < SIZE; ++i) {
        books[i]->print_book_type();
    }

    return 0;
}
