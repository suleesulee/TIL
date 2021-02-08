#include<stdio.h>
#include<stdlib.h>

typedef struct _node
{
    int data;
    struct _node *next;
}Node;

int main()
{
    Node* head = NULL;
    Node* cur = NULL;
    Node* tail = NULL;

    Node* newNode = NULL;
    int readData;

    while(1)
    {
        printf("input num: ");
        scanf("%d", &readData);

        if(readData < 1){
            break;
        }

        newNode = (Node*)malloc(sizeof(Node));
        newNode->data = readData;
        newNode->next = NULL;

        if(head == NULL){
            head = newNode;
            tail = newNode;
        }
        else {
            newNode->next = head;
            head = newNode;
        }
        
        
    }
    printf("\n");

    if(head == NULL){
        printf("None\n");
    } else {
        cur = head;
        printf("%d ", cur->data);
        while(cur->next != NULL){
            cur = cur->next;
            printf("%d ", cur->data);
        }
    }
    printf("\n\n");

    //Delete Node
    if(head == NULL){
        return 0;
    }
    else{
        Node* delNode = head;
        Node* delNodeNext = head->next;

        printf("%d delete\n" , head->data);
        free(delNode);

        while(delNode->next != NULL){
            delNode = delNodeNext;
            delNodeNext = delNodeNext->next;

            printf("%d delete\n", delNode->data);
            free(delNode);
        }
    }

    return 0;


}