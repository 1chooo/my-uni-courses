#include "stdio.h"
#include "stdlib.h"
#include <string.h>

//#include <bits/stdc++.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
struct Tree
{
	int data;
	struct Tree *left;
	struct Tree *right;
};
typedef struct Tree tree;
typedef struct Tree *p_tree;

p_tree createtree(int *, int, int);
void preorder(p_tree);
void inorder(p_tree);
void postorder(p_tree);
p_tree newNode(int);

int main()
{

	int n1;
	scanf("%d", &n1);
	getchar();
	int i;
	for (i = 0; i < n1; i++)
	{

		int num;
		scanf("%d", &num);
		getchar();
		if (num == 0)
		{
			return 0;
		}

		int data[num];
		int j;
		for (j = 0; j < num; j++)
		{
			scanf("%d", &data[j]);
			//			printf("%d ",data[j]);
		}

		p_tree root = createtree(data, 0, num);
		preorder(root);
		printf("\n");
		inorder(root);
		printf("\n");
		postorder(root);
		printf("\n");
		//		if(i != n1 - 1)
		//			printf("\n");
	}
	return 0;
}
p_tree newNode(int d)
{
	p_tree node = (p_tree)malloc(sizeof(tree));
	;
	node->data = d;
	node->left = node->right = NULL;
	return node;
}
p_tree createtree(int *a, int index, int num)
{

	p_tree root = NULL;
	if (index < num)
	{
		root = newNode(a[index]);

		// insert left child
		root->left = createtree(a, 2 * index + 1, num);

		// insert right child
		root->right = createtree(a, 2 * index + 2, num);
	}
	return root;
}

void preorder(p_tree ptr)
{

	if (ptr != NULL)
	{
		printf("%d ", ptr->data);
		preorder(ptr->left);
		preorder(ptr->right);
	}
}

void inorder(p_tree ptr)
{

	if (ptr != NULL)
	{
		inorder(ptr->left);
		printf("%d ", ptr->data);
		inorder(ptr->right);
	}
}

void postorder(p_tree ptr)
{

	if (ptr != NULL)
	{
		postorder(ptr->left);
		postorder(ptr->right);
		printf("%d ", ptr->data);
	}
}