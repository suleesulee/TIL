#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
	int n;
	int tri[501][501];
	int d[501][501];

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			scanf("%d", &tri[i][j]);
		}
	}
	
	d[1][1] = tri[1][1];

	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == 1) {
				d[i][1] = d[i - 1][1] + tri[i][1];
			}
			else if (j == i) {
				d[i][j] = d[i - 1][j - 1] + tri[i][j];
			}
			else {
				d[i][j] = max(d[i - 1][j - 1] + tri[i][j], d[i - 1][j] + tri[i][j]);
			}
		}
	}

	int max = d[n][1];
	for (int i = 1; i <= n; i++) {
		if (max < d[n][i]) {
			max = d[n][i];
		}
	}

	printf("%d", max);

	return 0;
}
/* ���̳������α׷��� ����
�׳� Ǯ���� .. ��ȭ�� ����� �׳� Ǯ�� �Ǵ� ��������
ù��°�� ��������°�� �� ���� �׳� ���ϸ� �Ǿ��� �߰��� ���� �ﰢ������ ������ ���Ҽ��ִ� ���߿� ū ���� �Ǵ°� �����ϸ�Ǿ���.*/