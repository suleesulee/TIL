#include "SimpleHeap.h"

void HeapInit(Heap *ph)
{
    ph->numOfData = 0;
}

int HIsEmpty(Heap *ph){
    if(ph->numOfData == 0)
        return TRUE;
    else
        return FALSE;
}

int GetParentIdx(int idx)
{
    return idx/2;
}

int GetLChildIdx(int idx)
{
    return idx*2;
}

int GetRChildIdx(int idx)
{
    return GetLChildIdx(idx) + 1;
}

int GetHiPriChildIdx(Heap *ph, int idx)
{
    if(GetLChildIdx(idx) > ph->numOfData)
        return 0;
    else if(GetLChildIdx(idx) == ph->numOfData)
        return GetLChildIdx(idx);
    else
    {
        if(ph->heapArr[GetLChildIdx(idx)].pr > ph->heapArr[GetRChildIdx(idx)].pr)
            return GetRChildIdx(idx);
        else
            return GetLChildIdx(idx); 
    }
}

void HInsert(Heap *ph, HData data, Priority pr)
{
    int idx = ph->numOfData + 1;
    HeapElem nelem = {pr, data};

    while(idx != 1)
    {
        if(pr < (ph->heapArr[GetParentIdx(idx)].pr))
        {
            ph->heapArr[idx] = ph->heapArr[GetParentIdx(idx)];
            idx = GetParentIdx(idx);
        }
        else
            break;
    }
    ph->heapArr[idx] = nelem;
    ph->numOfData += 1;
}

HData HDelete(Heap *ph)
{
    HData retData = (ph->heapArr[1]).data;
    HeapElem lastElem = ph->heapArr[ph->numOfData];

    int parentIdx = 1;
    int childIdx;

    while(childIdx = GetHiPriChildIdx(ph, parentIdx))
    {
        if(lastElem.pr <= ph->heapArr[childIdx].pr)
            break;
        ph->heapArr[parentIdx] = ph->heapArr[childIdx];
        parentIdx = childIdx;
    }

    ph->heapArr[parentIdx] = lastElem;
    ph->numOfData -= 1;
    return retData;
}

