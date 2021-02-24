#include<cstdio>
#include<cstring>

#define MAX 100001

using namespace std;

int n;
int arr[MAX];
int change_arr[MAX];
int flag = 0;
int temp;





int main() {
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}

	if (n % 2 == 0) {	//nÀÌ Â¦¼öÀÏ¶§
		even();
	}
	else {				//nÀÌ È¦¼öÀÏ¶§
		odd();
	}

	return 0;
}