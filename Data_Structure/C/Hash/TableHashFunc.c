#include<stdio.h>

typedef struct _empInfo
{
    int empNum;
    int age;
}EmpInfo;

int GetHashValue(int empNum){
    return empNum % 100;
}

int main(){
    EmpInfo empInfoArr[100];
    EmpInfo emp1 = {20200003, 32};
    EmpInfo emp2 = {20202003, 42};
    EmpInfo emp3 = {20204003, 22};

    EmpInfo r1, r2, r3;

    empInfoArr[GetHashValue(emp1.empNum)]=emp1;
    empInfoArr[GetHashValue(emp2.empNum)]=emp2;
    empInfoArr[GetHashValue(emp3.empNum)]=emp3;

    r1 = empInfoArr[GetHashValue(20200003)];

    print("사번 : %d, 나이: %d \n", r1.empNum, r1.age);

    return 0;
}
