#include<cstdio>
#include<cmath>

int n;
int main() {
	int cnt = 0;

	scanf("%d", &n);

	if (n == 1){
		cnt = 10;
	}
	else {
		int nw = pow(10, n);
		for (int i = nw; i < nw*10; i++) {

		}

	}



	printf("%d", cnt);

	return 0;
}