#include<stdio.h>
#include"ExpressionTree.h"

int main()
{
    char exp[] = "12+7*";
    BTreeNode* eTree = MakeExpTree(exp);

    ShowPrefixTypeExp(eTree);
    printf("\n");

    ShowInfixTypeExp(eTree);
    printf("\n");

    ShowPostfixTypeExp(eTree);
    printf("\n");

    EvaluateExpTree(eTree);    
}