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

/*���̳��� ���α׷��� ����
���� �Դ� �������� ���� �ִ��� ��츦 �����ϸ�
1. ���� �����ָ� �ȸԴ� ���  
2. ���� �����ָ� �԰� ������ �ȸ��� ���
3. ���� �����ֿ� ������ ���� ���

3��° �����ָ� ������
1,2 ���� ���� ���
1,3 ���� ���� ���
2,3 ���� ���� ��� 

�� �߿� ���� ū ���� ���ϸ� �ȴ�.

���̳��� ���α׷��� ������ ��ȭ���� �߿��ϴ�.. 
�𸣰ڴٸ� �Ѿ��� ��Ǯ���� �� ����.

3��° �����ֿ��� �ش� �����ָ� �Ȱ����� �Ѿ�� ���̽��� �־ ��ٷο� �� ����.


*/