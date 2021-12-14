#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main() {
	
	char in1[1001];
	char in2[1001];
	int len1 = 0;
	int len2 = 0;

	scanf("%s %s", in1, in2);

	len1 = strlen(in1);
	len2 = strlen(in2);
	int dp[len1 + 1][len2 + 1];

	for (int i = 0; i <= len1; i++) {
		for (int j = 0; j <= len2; j++) {
			dp[i][j] = 0;
		}
	}

	for (int i = 1; i <= len1; i++) {
		for (int j = 1; j <= len2; j++) {
			if (in1[i - 1] == in2[j - 1])
				dp[i][j] = dp[i - 1][j - 1] + 1;
			else
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}

	printf("%d", dp[len1][len2]);

	return 0;
}

/*다이나믹 프로그래밍 문제.. 골드5
이런게 골드5문제라니;;; 푸는방법을 봐도 이해가 잘 안된다..
dp나오면 쥐약이 되겠군.. 
문자를 하나씩 비교해서 같으면 +1 아니면 max(위쪽, 왼쪽) 값을 가진다
dp 문제보다 다른 문제를 풀어봐야겠다..
*/