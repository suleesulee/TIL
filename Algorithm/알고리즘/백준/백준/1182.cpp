#include<cstdio>
int n, s;
int arr[20];
int cnt = 0;
void cal(int idx, int sum) {
	sum += arr[idx];
	//기저사례
	if (idx >= n)
		return;
	if (sum == s)
		cnt++;
	//현재것을 안더할때
	cal(idx + 1, sum - arr[idx]);
	//현재것을 더할떄
	cal(idx + 1, sum);
}

int main()
{
	scanf("%d %d", &n, &s);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	cal(0, 0);

	printf("%d", cnt);


	return 0;
}