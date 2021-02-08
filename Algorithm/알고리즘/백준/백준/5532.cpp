#include<cstdio>
#include<cstring>

using namespace std;

int l, a, b, c, d;
int korean, math;
int res;

int main() {
    scanf("%d", &l);
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);

    if(a%c == 0)
        korean = (a / c);
    else
        korean = (a / c) + 1;
    
    if(b%d == 0)
        math = (b / d);
    else
        math = (b / d) + 1;

    if (korean > math) {
        res = l - korean;
    }
    else {
        res = l - math;
    }

    printf("%d", res);
}