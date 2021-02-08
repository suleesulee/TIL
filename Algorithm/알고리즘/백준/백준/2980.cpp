#include<cstdio>
#include<cstring>

#define MAX 100
using namespace std;

int N, L;
int sinho[MAX][4];
int truck_d = 0;
int time = 0;
int x = 0;

int main() {
	scanf("%d %d", &N, &L);

	for (int i = 0; i < N; i++) {
		scanf("%d %d %d", &sinho[i][0], &sinho[i][1], &sinho[i][2]);
		sinho[i][3] = 0;	//default : 빨간불
	}

	while (truck_d != L) {
		if (sinho[x][0] == truck_d)	//트럭이랑 신호등이랑 만날때
		{
			while (0 <= time % (sinho[x][1] + sinho[x][2]) && time % (sinho[x][1] + sinho[x][2]) < sinho[x][1])
			{
				time++;
			}

			truck_d++;
			time++;
			x++;
		}
		else    //트럭이랑 신호등이랑 안만날때
		{
			truck_d++;
			time++;
		}
 	}


	printf("%d", time);

	return 0;
}