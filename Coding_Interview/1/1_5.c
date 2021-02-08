#include<stdio.h>
#include<string.h>
#include<math.h>

#define FALSE 0
#define TRUE 1

int sub_str(char *str1, char *str2)
{
    int str_len1, str_len2;
    int cmp;
    int diff = 0;

    str_len1 = strlen(str1);
    str_len2 = strlen(str2);
    

    if(abs(str_len1 - str_len2) > 1)
        return FALSE;

    if(str_len1 > str_len2){
        cmp = str_len2;
    }
    else{
        cmp = str_len1;
    }


    for(int i = 0; i < cmp; i++){
        if(str1[i] != str2[i])
            diff++;

        if(diff > 1)
            return FALSE;
    }   
}

int Editreplace(char *str1, char *str2)
{
    int diff = FALSE;
    for(int i = 0; i < strlen(str1); i++){
        if(str1[i] != str2[i])
            if(diff){
                return FALSE;
            }
            diff = TRUE;
    }
}

int oneEditInsert(char *str1, char *str2)
{
    int index1 = 0;
    int index2 = 0;
    while(index2 < strlen(str2) && index1 < strlen(str1)){
        if(str1[index1] != str2[index2]){
            if(index1 != index2)
                return FALSE;
            index2++;
        } else {
            index1++;
            index2++;
        }
    }
    return TRUE;
}