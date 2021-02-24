#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int duplication(char* str){
    //ASCII는 128자

    if(str.lenth()>128)
        return false;

    int char_set[128] = {0,}

    for(int i = 0; i<str.len(); i++){
        int val = (int)str[i];
        if(char_set[val] == 0){
            char_set[val] = 1;
        } else {
            return false;
        }
    }

    return true;     
}