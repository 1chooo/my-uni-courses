# Chapter5 Trees

### Binary Tree

A finite set of nodes either empty or consisting of a root node, left and right binary tree.

1. create()
2. IsEmpty()
3. MakeBinaryTree
4. Lchild()
5. Data
6. Rchild

The maximum number of nodes on level i of a binary tree is $2^{i-1}, i >= 1$

The maximum number of nodes in a binary tree of depth k is $2^{i-1}, i >= 1$


### Insert A Node into a threaded Binary Tree

1. change `parent->right_thread` into `FALSE`
2. set `child->left_thread` and `child->right_thread` into `TRUE`
3. set `child->left_child` point to parent
4. set `child->right_child` to `parent->right_child`
5. change `parent->right_child` point to `child`