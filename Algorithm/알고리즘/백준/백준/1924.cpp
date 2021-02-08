#include<cstdio>
int m, d;
char date[7][4] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
int arr[11] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 };
int main() {
	scanf("%d %d", &m, &d);

	int sum = 0;
	int ans; 
	if (m > 1) {
		for (int i = 0; i < m - 1; i++) {
			sum += arr[i];
		}
	}
	sum += d;
	ans = sum % 7;

	printf("%s", date[ans]);

	return 0;
}