#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_SIZE 100000

typedef struct node {
    char value;
    struct node *link;
} Node;

Node *createNode(char);
Node *createNode(Node*);
Node *mergeLists(Node*, Node*);
Node *reverse(Node*);

void showAns();

int main(void) {
    int N, M, index;
    Node *L1 = NULL, *L2 = NULL, *ans = NULL;
    Node *temp = NULL, *lastNode = NULL;

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        char value;

        scanf("%c", &value);
        temp = createNode(value);

        if (i == 0) {
            L1 = temp;
            lastNode = temp;
        } else {
            lastNode->link = temp;
            lastNode = temp;
        }
    }

    printf("%c", L1[1].value);

    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
        char value;

        scanf("%c", &value);
        temp = createNode(value);

        if (i == 0) {
            L2 = temp;
            lastNode = temp;
        } else {
            lastNode->link = temp;
            lastNode = temp;
        }
    }

    scanf("%d", &index);   
  

    return 0;
}

Node *createNode(char value) {
    Node *newNode = (Node *) malloc(sizeof(Node));
    newNode->value = value;
    newNode->link = NULL;

    return newNode;
}

Node *mergeLists(Node *a, Node *b) {
    Node *head = NULL;
    
    for (Node **link = &head;; link = &(*link)->link) {
        if (a == NULL) {
            *link = b;
            break;
        }
        if (b == NULL) {
            *link = a;
            break;
        }
        if (a->value <= b->value) {
            *link = a;
            a = a->link;
        } else {
            *link = b;
            b = b->link;
        }
    }
    return head;
}

Node *reverse(Node *head){
    Node *result = NULL;
    while (head) {
        Node *next = head->link;
        head->link = result;
        result = head;
        head = next;
    }

    return result;
}

void showAns(Node *ans) {

  while (ans) {
    print("%c-->", ans->value);
    ans = ans->link;
  }
  print("-->NULL\n");

  return;
}