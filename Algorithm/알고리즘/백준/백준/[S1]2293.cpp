#include<cstdio>

int n, k;
int coin[101] = { 0 };
int d[10001] = { 0 };

int main() {
	
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &coin[i]);
	}
	d[0] = 1; //하나도 선택안하는 경우

	for (int i = 1; i <= n; i++) {
		for (int j = coin[i]; j <= k; j++) {
			d[j] += d[j - coin[i]];
		}
	}
	printf("%d", d[k]);

}

/* 다이나믹프로그래밍 문제
일단 다이나믹프로그래밍은 점화식부터 찾아야하는것 같다.
사실 잘모르겠어서 점화식관련해서 찾아봄..
아직 이런문제들이 나오면 어찌해야할지 감을 못잡는것 같다.


*/