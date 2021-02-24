#include<cstdio>
int a, b, c;
long long mul;
int arr[10] = { 0, };
int tmp; 

int main()
{
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	mul = a * b * c;

	while (mul > 10) {
		tmp = mul % 10;
		mul = mul / 10;
		arr[tmp]++;
	}
	arr[mul]++;

	for (int i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}

	return 0;
}