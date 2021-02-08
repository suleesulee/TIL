#include<cstdio>
#include<cstring>

using namespace std;

long broken;
long num;
long long int res;

int main() {
	scanf("%d", &broken);
	scanf("%d", &num);

	if (broken == 1) {
		res = 8 * num;
	}
	else if (broken == 5) {
		res = 4 + (num * 8);
	}
	else if (broken == 2) {
		if (num % 2 == 0)
			res = 1 + (8 * num / 2);
		else
			res = (8 * ((num / 2) + 1)) - 1;
	}
	else if (broken == 3) {
		res = 2 + (num * 4);
	}
	else if (broken == 4) {
		if (num % 2 == 0)
			res = 3 + (8 * num / 2);
		else
			res = (8 * ((num / 2) + 1)) - 3;
	}
	printf("%lld", res);

	return 0;
}