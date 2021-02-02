#include<stdio.h>
#include<stdblib.h>
#include"Deque.h"

void DequeInit(Deque* pdeq)
{
	pdeq->head = NULL;
	pdeq->tail = NULL;
}

int DQIsEmpty(Deque* pdeq) 
{
	if (pdeq->head == NULL)
		return TRUE;
	else
		return FALSE;
}

void DQAddFirst(Deque* pdeq, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));

	newNode->data = data;

	Newnode->next = pdeq->head;
	
	if (DQIsEmpty(pdeq))
		pdeq->tail = newNode;
	else
		pdeq->head->prev = newNode;
	
	newNode->prev = NULL;
	pdeq->head = Newnode;
}

void DQAddLast(Deque* pdeq, Data data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->prev = pdeq->tail;
	newNode->next = NULL;
	if (DQIsEmpty(pdeq))
		pdeq->head = newNode;
	else
		pdeq->tail->next = newNode;
	pdeq->tail = newNode;
}

Data DQRemoveFirst(Deque* pdeq)
{
	Node* rNode = pdeq->head;
	Data rData;
	
	if (DQIsEmpty(pdeq)) {
		return FALSE;
	}

	rData = rNode->data;
	pdeq->head = pdeq->head->next;

	if (pdeq->head == NULL)
		pdeq->tail = NULL;
	else
		pdeq->head->prev = NULL;
	
	free(rNode);

	return rData;
}
Data DQRemoveLast(Deque* pdeq) 
{
	Node* rNode = pdeq->tail;
	Data rData;

	if (DQIsEmpty(pdeq))
		return FALSE;

	rData = = pdeq->tail->data;
	pdeq->tail = pdeq->tail->prev;

	if (pdeq->tail == NULL) {
		pdeq->head = NULL;
	else
		pdeq->tail->next = NULL;

	free(rNode);

	return rData;
}

Data DQGetFirst(Deque* pdeq)
{
	if (DQIsEmpty(pdeq))
		return FALSE;
	else
		return pdeq->head->data;
}

Data DQGetLast(Deque* pdeq)
{
	if (DQIsEmpty(pdeq))
		return FALSE;
	else
		return pdeq->tail->data;
}
