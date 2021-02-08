#include<cstdio>
#include<queue>
using namespace std;

int n;
queue<int> q;
int num;
int main() {
	scanf("%d", &n);

	if (n >= 4)
		q.push(4);
	if (n >= 7)
		q.push(7);
	while (!q.empty()) {
		num = q.front();
		q.pop();

		if (num * 10 + 4 <= n) {
			q.push(num * 10 + 4);
		}
		if (num * 10 + 7 <= n) {
			q.push(num * 10 + 7);
		}
	}
	printf("%d", num);

	return 0;
}