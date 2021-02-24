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

/*���̳��� ���α׷��� ����.. ���5
�̷��� ���5�������;;; Ǫ�¹���� ���� ���ذ� �� �ȵȴ�..
dp������ ����� �ǰڱ�.. 
���ڸ� �ϳ��� ���ؼ� ������ +1 �ƴϸ� max(����, ����) ���� ������
dp �������� �ٸ� ������ Ǯ����߰ڴ�..
*/