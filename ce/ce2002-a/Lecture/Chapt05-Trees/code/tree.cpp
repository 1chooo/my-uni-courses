#include <iostream>
#include <cstdlib>


class Tree;
class TreeNode{
    TreeNode *leftchild;   // 以下表示每一個node有四個pointer指向child
    TreeNode *rightchild;
    TreeNode *whatever;
    TreeNode *works;
    int data1;             // node所攜帶的information
    double data2;
    ...
    friend class Tree;     // 讓class Tree能夠存取TreeNode的private data
};
class Tree{
    TreeNode *root;        // 以root作為存取整棵樹的起點
};