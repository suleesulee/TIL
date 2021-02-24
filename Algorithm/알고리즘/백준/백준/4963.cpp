#include<cstdio>
#include<queue>

using namespace std;


int width, height;
int map[50][50] = { 0, };
int visited[50][50] = { 0, };
int dx[8] = {1, 1, 0, -1, -1, -1, 0 , 1};
int dy[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };

void init() {
	
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			map[i][j] = 0;
		}
	}
}

void cal(int x, int y) {

}


int main()
{


	while (1) {
		scanf("%d %d", width, height);

		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				scanf("%d", &map[i][j]);
			}
		}

	}




	return 0;
}