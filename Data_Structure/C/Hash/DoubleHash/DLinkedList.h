#ifndef __D_LINKED_LIST__H__
#define __D_LINKED_LIST__H__

#include "Slot2.h"

typedef Slot LData;
typedef struct _node
{
    LData data;
    struct _node *next;
} Node;

typedef struct _linkedList
{
    Node* head;
    Node* cur;
    Node* before;
    int numOfData;
    int (*comp)(LData d1, LData d2);
}LinkedList;

#endif