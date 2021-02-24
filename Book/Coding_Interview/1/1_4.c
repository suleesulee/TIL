#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int table[26] = {0,};

int palined(char input[])
{
    int res;
    buildTable(/*string*/);
    res = findOdd();
    return  res;
}

void buildTable(char input[])
{
    int len = strlen(input);
    for(int i = 0; i < len ; i++)
    {
        int tmp = input[i] - 97;
        table[tmp]++;
    }
}

int findOdd(void)
{
    int odd = 0;

    for(int i =0 ;i<26; i++)
    {
        if(table[i]%2 != 0)
            odd ++;
    }
    if(odd != 1)
        return 0;
    else 
        return 1;
}