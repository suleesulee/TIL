#include<stdio.h>
#include"BinaryTree.h"

void InoederTraverse(BTreeNode* bt)
{
    if(bt == NULL)
        return ;
    InoederTraverse(bt->left);
    printf("%d \n", bt->data);
    InorderTraverse(bt->right);

}