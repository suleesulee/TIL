#include<cstdio>

using namespace std;

int N;
char temp;
int map[51][5][7];
int s = 1;
int diff = 0;
int min = 1000000;
int min1 = 0;
int min2 = 0;

void solve(int start) {
	for (int k = start + 1; k <= N; k++) {
		diff = 0;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 7; j++) {
				if (map[start][i][j] != map[k][i][j])
					diff++;
			}
		}
		if (min > diff) {
			min = diff;
			min1 = start;
			min2 = k;
		}
	}
}

int main() 
{
	scanf("%d", &N);
	getchar();

	for (int k = 1; k <= N; k++) {
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 7; j++) {
				scanf("%1c", &temp);
				if (temp == '.')
					map[k][i][j] = 0;
				else
					map[k][i][j] = 1;
			}
			getchar();
		}
	}

	for(int i = s; s<=N; s++)
		solve(s);
	
	printf("%d %d", min1, min2);
	return 0;
}