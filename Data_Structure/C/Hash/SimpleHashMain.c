#include<stdio.h>
#include<stdlib.h>
#include"Person.h"
#include"Table.h"

int MyHashFunc(int k)
{
    return k % 100;
}

int main(){
    Table myTbl;
    Person *np;
    Person *sp;
    Person *rp;

    TBLInit(&myTbl, MyHashFunc);

    np = MakePersonData(20120003, "lee", "Seoul");
    TBLInsert(&myTbl, GetSSN(np), np);
    np = MakePersonData(20120013, "lee", "Seoul");
    TBLInsert(&myTbl, GetSSN(sp), sp);
    np = MakePersonData(20120043, "lee", "Seoul");
    TBLInsert(&myTbl, GetSSN(rp), rp);

    sp = TBLSearch(&myTbl, 20120003);
    if(sp != NULL)
        ShowPerInfo(sp);
    
    rp = TBLDelsete(&myTbl, 20120003);
    if(rp != NULL)
        free(rp);
}