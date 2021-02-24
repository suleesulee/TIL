#include<cstdio>
#include<cstring>

using namespace std;

#define MAX 1001
int n, m, l;

int ans = 0;
int people[MAX];
int ball = 1;

int main() {
	memset(people, 0, sizeof(people));
	scanf("%d %d %d", &n, &m, &l);
	
	people[1] = 1;

	while (1) {
		if (people[ball] % 2 == 0) {
			if (ball + l >= n) {
				ball = l - n + ball;
			}
			else
				ball += l;
			//printf("ball : %d\n", ball);
		}
		else {
			if(ball - l < 0){
				ball = n - l + ball;
			}
			else
				ball -= l;
			//printf("ball : %d\n", ball);
		}

		ans++;
		people[ball]++;
		if (people[ball] == m)
			break;
	}
		
	printf("%d", ans);
	return 0;
}