#include <stdio.h>
#include <stdlib.h>
#include "Person.h"
#include "Table2.h"

int MyHashFunc(int k){
    return k % 100;
}

int main(){
    Table myTbl;
    Person *np;
    Person *sp;
    Person *rp;

    TBLInit(&myTbl, MyHashFunc);

    np = MakePersonData(99999, "LEe", "SSe");
    TBLInsert(&myTbl, GetSSN(np), np);
    
    sp = TBLSearch(&myTbl, 99999);
    if(sp != NULL)
        ShowPerInfo(sp);

    rp = TBLDelete(&myTbl, 99999);
    if(rp != NULL)
        free(rp);

    return 0;
}