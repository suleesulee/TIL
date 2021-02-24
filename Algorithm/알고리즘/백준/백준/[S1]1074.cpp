#include<cstdio>
#include<cmath>

int main() {
	int n, r, c;
	int len;
	int x, y;
	int ans = 0;

	scanf("%d %d %d", &n, &r, &c);

	len = pow(2, n);
	
	x = len / 2;
	y = x;

	/*
	  1   |   2
	      |
	-------------
	  3   |   4
		  |
	*/

	while (n-- > 0) {
		int tmp = pow(2, n) / 2;
		int skip = pow(4, n);
		
		if (r < y && c < x) {
			x -= tmp;
			y -= tmp;
		}
		else if (r < y && x <= c) {
			x += tmp;
			y -= tmp;
			ans += skip;// 앞 사분면을 스킵한 값
		}
		else if (r >= y && c < x) {
			x -= tmp;
			y += tmp;
			ans += skip * 2;
		}
		else {
			x += tmp;
			y += tmp;
			ans += skip * 3;
		}
	}

	printf("%d", ans);
	return 0;
}

/*분할정복을 통한 풀이를 사용했다.
스킵을 하며 찍어나가야하는것은 내가 세운 풀이과정에 들어간다.
다만 어느부분에서 r,c를 만족하는 값을 찾아서 돌아야하는지 헤매다
x,y 값을 사용해야한다는것을 알았다.
n값으로 사분할 한뒤 필요없는 분면은 스킵으로 더하고 tmp 값을 x,y 값에 분면의 좌상단의 값을 넣어
계속해서 재귀적으로 돌려서 마지막 4칸까지 r,c를 찾는과정을 반복해
해당 r,c를 언제 방문하는지 얻어냈다.

*/