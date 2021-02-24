#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int n;
	int wine[10003];
	int dp[10003] = { 0 };

	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &wine[i]);
	}

	dp[1] = wine[1];
	dp[2] = wine[2] + wine[1];


	for (int i = 3; i <= n; i++) {
		dp[i] = max(dp[i - 3] + wine[i] + wine[i - 1], dp[i - 2] + wine[i]);
		dp[i] = max(dp[i - 1], dp[i]);
	}

	printf("%d", dp[n]);

	return 0;
}

/*다이나믹 프로그래밍 문제
현재 먹는 포도주의 합의 최대인 경우를 생각하면
1. 현재 포도주를 안먹는 경우  
2. 현재 포도주를 먹고 이전걸 안먹은 경우
3. 현재 포도주와 이전걸 먹은 경우

3번째 포도주를 먹을때
1,2 번을 먹은 경우
1,3 번을 먹은 경우
2,3 번을 먹은 경우 

셋 중에 가장 큰 값을 구하면 된다.

다이나믹 프로그래밍 문제는 점화식이 중요하다.. 
모르겠다면 한없이 안풀리는 것 같다.

3번째 포도주에서 해당 포도주를 안고르고 넘어가는 케이스가 있어서 까다로운 것 같다.


*/