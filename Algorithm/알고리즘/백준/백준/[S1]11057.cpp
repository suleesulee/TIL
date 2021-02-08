#include<cstdio>
#include<algorithm>

int d[1001][10];

int main() {
	int n;
	int mod = 10007;
	int sum = 0;
	
	scanf("%d", &n);
	
	for (int i = 0; i <= 9; i++) {
		d[1][i] = 1;
	}

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j <= 9; j++) {
			for (int k = j; k <= 9; k++) {
				d[i][k] += d[i - 1][j];
				d[i][k] %= mod;
			}
		}
	}
	for (int i = 0; i <= 9; i++) {
		sum += d[n][i];
	}

	printf("%d", sum % mod);
	
	return 0;
}

/*다이나믹 프로그래밍 문제
와 전혀 이런식으로 생각할줄은 몰랐다..
아직 내 실력이 너무 부족한것 같다..
마지막자리수를 통해 앞자리를 값을 더해나가는 방법을 사용해 점화식을 만들어내다니
실버1문제라 잘하는 분들은 별 어려운 없이 풀어낼 것 같다.
그래도 일단 이해는 되었으니 비슷한 문제가 나오면 어떻게든 해결해보려 할 것 같다.
*/