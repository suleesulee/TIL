#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<map>
using namespace std;

int tc;
char number[7];
int token_num[7];
int prime[10000000];

int check_num(char* in) {
	int size;
	size = strlen(in);
	for (int i = 0; i < size; i++) {
		token_num[i] = in[i] - '0';
		//printf("%d ", token_num[i]);
	}
	return size;
}

int assemble(int size) {
	int ans = 0;
	sort(token_num, token_num + size);
	//printf("%d", token_num[0]);
	map<int, int> m;
	do {
		int x = 0;
		for (int i = 0; i < size; i++) {
			x = 10 * x + token_num[i];
			if (m.find(x) != m.end()) continue;
			m[x] = 1;
			if (prime[x]) ans++;
		}
	} while (next_permutation(token_num, token_num + size));
	return ans;
}

void erastenos() {
	memset(prime, 1, sizeof(prime));
	prime[0] = 0;
	prime[1] = 0;
	for (int i = 2; i < 10000000; i++) {
		if (prime[i] == 0)
			continue;
		for (int j = i + i; j < 10000000; j += i) {
			prime[j] = 0;
		}
	}
}
int main() {
	erastenos();
	int size;
	
	scanf("%d", &tc);

	for (int i = 0; i < tc; i++) {
		int ans = 0;
		scanf("%s", &number);
		size = check_num(number);
		ans = assemble(size);
		printf("%d\n", ans);
	}

	//for (int i = 0; i < 7; i++) {
	//	printf("%s ", ch_num[i]);
	//}

}