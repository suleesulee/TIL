#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int change_blank(char arr[], int len)
{
    char *change = NULL;
    int space = 0;
    for(int i=0; i<len; i++)
    {
        if(arr[i] == ' ')
            space++;
    }

    int index = len + space*2;
    int index_temp = 0;
    change = (char*)malloc(index);
    
    for(int i = 0; i<len + space*2 ;i++)
    {
        if(arr[i] == ' ')
        {
            change[i] ='%';
            change[i+1] ='2';
            change[i+2] ='0';
            index_temp+=3;
        }
        else{
            change[index_temp] = arr[i];
            index_temp+=1;
        }
    }
}