#include<cstdio>
#include<cmath>

long long pow(int a, int b, int c) {
	if (b == 1)
		return a;
	else
	{
		long long temp = pow(a, b / 2, c);

		if (b % 2)
			return ((temp * temp) % c * a) % c;
		else
			return (temp * temp) % c;
	}

}

int main() {

	int a, b, c;
	long long temp;

	scanf("%d %d %d", &a, &b, &c);	
	//((a % c) ^ b) % c

	//temp = pow(a % c, b, c);

	long ans = 1;
	long mul = a % c;

	while (b > 0) {
		if (b % 2 == 1) {
			ans *= mul;
			ans %= c;
		}
		mul = ((mul % c) * (mul % c)) % c;
		b /= 2;
	}

	printf("%ld", ans);
	//printf("%lld", temp);

	return 0;
}

/*���й��� ���� ����� �������� ������ ���� ������ �����ؾ� Ǯ���־���..
* 
* Ǯ�̹��� �ѹ� �� ���߰ڴ�..  ���� ���Ŀ� ���� ���ذ� ���� �ʾҴ�...

*/