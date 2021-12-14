#include<cstdio>
int ans = 0;
int tmp; 
int main()
{
	for (int i = 0; i < 5; i++) {
		scanf("%d", &tmp);
		if (tmp < 40)
			ans += 40;
		else
			ans += tmp;
	}
	printf("%d", ans / 5);

	return 0;
}