#include<stdio.h>
#include<stdlib.h>
#include"DBLinkedList.h"

void ListInit(List *plist){
    plist->head = NULL;
    plist->numOfData = 0;
}

void LInsert(List *plist, Data data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;

    newNode->next = plist->head; //현재 head를 newNode의 next로 옮김
    if(plist->head != NULL)     //head가 NULL이 아니면 head의 prev도 newNode를 가르킴
        plist->head->prev = newNode;

    newNode->prev = NULL;   //새노드의 prev는 NULL
    plist->head = newNode;  //head는 newNode를 가르킴

    plist->numOfData++;
}

int LFirst(List *plist, Data *pdata){
    if(plist->head == NULL)
        return FALSE;
    
    plist->cur = plist->head;
    *pdata = plist->cur->data;

    return TRUE;
}

int LNext(List *plist, Data *pdata)
{
    if(plist->cur->next == NULL)
        return FALSE;
    
    plist->cur = plist->cur->next;
    *pdata = plist->cur->data;

    return TRUE;
}

int LPrevious(List *plist, Data *pdata)
{
    if(plist->cur->prev == NULL)
        return FALSE;
    
    plist->cur = plist->cur->prev;
    *pdata = plist->cur->data;

    return TRUE;
}

int LCount(List *plist)
{
    return plist->numOfData;
}