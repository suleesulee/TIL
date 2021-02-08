#include<cstdio>
int x, y, w, h;
int ans[4];

int main()
{
	scanf("%d %d %d %d", &x, &y, &w, &h);

	ans[0] = x - 0;
	ans[1] = w - x;
	ans[2] = y - 0;
	ans[3] = h - y;

	int tmp = ans[0];

	for (int i = 1; i < 4; i++) {
		if (tmp > ans[i])
			tmp = ans[i];
	}
	printf("%d", tmp);

	return 0;
}