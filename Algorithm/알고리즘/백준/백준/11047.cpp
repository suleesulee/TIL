#include<cstdio>
using namespace std;

int main()
{
	int n, k;
	int money[10] = { 0, };
	int max = 0;
	int money_cnt = 0;


	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		scanf("%d", &money[i]);
	}

	for (int i = 0; i < n; i++) {
		if (money[i] < k) {
			max++;
		}
	}

	for (int i = max; i < 0; i--) {
		if (k == 0)
			break;
		else if (money[i] > k)
			continue;
			
		money_cnt += k/money[i];
		k %= money[i];
	}

	printf("%d", money_cnt);

	return 0;
}