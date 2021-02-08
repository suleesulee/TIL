#include<cstdio>
#include<cstring>

using namespace std;

int n, l;
int map[101][101];
int cnt = 0;
int flag = 0;
int flag2 = 0;

void find() {
	//for (int i = 1; i <= n; i++) {
	//	int temp = map[i][1];
	//	for (int j = 1; j <= n; j++) {
	//		if (temp != map[i][j]) {
	//			break;
	//		}
	//		else if (j == n) {
	//			cnt++;
	//		}
	//	}
	//}

	for (int i = 1; i <= n; i++) {
		int temp = map[1][i];
		for (int j = 1; j <= n; j++) {
			if (temp != map[j][i])
				break;
			else if (j == n) {
				cnt++;
			}
		}
	}

	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if (map[i][j] != map[i][j + 1] && map[i][j] > map[i][j + 1]) {
				int temp = map[i][j + 1];
				//printf("temp1 : %d\n", temp);
				for (int k = j + 1; k < j + 1 + l; k++) {
					if (temp != map[i][k]) {
						flag = 1;
						break;
					}
				}
				if (flag == 1) {
					flag = 0;
					break;
				}
			}
			else if (map[i][j] != map[i][j + 1] && map[i][j] < map[i][j + 1]) {
				break;
			}

			if (j == n - 1) {
//				printf("map :%d\n ", i);
				cnt++;
			}
		}
	}

	for (int i = n; i > 1; i--) {
		for (int j = n; j > 1; j--) {
			if (map[i][j] != map[i][j - 1] && map[i][j] < map[i][j - 1]) {
				int temp = map[i][j - 1];
				//printf("temp2 : %d\n", temp);
				for (int k = j - 1; k > j - 1 - l; k--) {
					if (temp != map[i][k]) {
						flag = 1;
						flag2 = 1;
						break;
					}
				}
				if (flag == 1) {
					flag = 0;
					break;
				}
			}
			else if (map[i][j] != map[i][j - 1] && map[i][j] > map[i][j - 1]) {
				break;
			}
			if (j == 2 && flag2 == 1) {
				//printf("map :%d\n ", i);
				cnt++;
				flag2 = 0;
			}
			else {
				flag2 = 0;
			}


		}
	}
	printf("%d", cnt);
}

int main() {
	scanf("%d %d", &n, &l);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
		}
	}

	// for (int i = 1; i <= n; i++) {
	// 	for (int j = 1; j <= n; j++) {
	// 		printf("%d ", map[i][j]);
	// 	}
	// 	printf("\n");
	// }

	find();

	return 0;
}