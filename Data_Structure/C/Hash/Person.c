#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"person.h"

int GetSSN(Person *p)
{
    return p->ssn;
}

void ShowPersonInfo(Person *p)
{
    printf("주민등록번호: %d\n", p->ssn);
    printf("이름: %s\n", p->name);
    printf("주소: %s\n\n", p->addr);
}

Person *MakePersonData(int ssn, int name, int addr){
    Person *newP = (Person*)malloc(sizeof(Person));
    newP->ssn = ssn;
    strcpy(newP->name, name);
    strcpy(newP->addr, addr);
}

