#include<cstdio>
#include<algorithm>

using namespace std;

int n;
int num[12];
int oper[4];
int Max = -1000000000;
int Min = 1000000000;


void dfs(int idx, int plus, int minus, int multi, int div, int total) {
	if (idx == n) {
		Max = max(Max, total);
		Min = min(Min, total);
	}
	if(plus < oper[0])
		dfs(idx + 1, plus + 1, minus, multi, div, total + num[idx]);
	if (minus < oper[1])
		dfs(idx + 1, plus, minus + 1, multi, div, total - num[idx]);
	if (multi < oper[2])
		dfs(idx + 1, plus, minus, multi + 1, div, total * num[idx]);
	if (div < oper[3])
		dfs(idx + 1, plus, minus, multi, div + 1, total / num[idx]);
}

int main() {
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}
	for (int i = 0; i < 4; i++)	{
		scanf("%d", &oper[i]);
	}

	dfs(1, 0, 0, 0, 0, num[0]);

	printf("%d\n%d", Max, Min);

	return 0;
}