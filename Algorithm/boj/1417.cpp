#include<cstdio>
#include<cstring>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int n;
int dasom;
int temp;
vector<int> v;
int badman = 0;

/*int arr[1001];
int max = -1;
int badman = 0;
int temp1;
int temp2;
int cnt = 0;
*/



int main() {

	cin >> n;
	cin >> dasom;
	
	for (int i = 0; i < n - 1; i++) {
		cin >> temp;
		if (temp >= dasom) {
			v.push_back(temp);
		}
	}

	if (n == 1) {
		printf("0");
		return 0;
	}

	

	while (v.size() != 0) {
		sort(v.begin(), v.end());
		if (dasom > v[v.size() - 1])
			break;
		v[v.size() - 1]--;
		dasom++;
		badman++;
	}

	cout << badman;

	return 0;

	//큰수가 들어오면 감당을 못함 
	/*while (1) {
		for (int i = 1; i <= n; i++) {	//가장 많은 표를 받는 것을 구함
			if (max < arr[i]) {
				max = arr[i];
			}
		}

		for (int i = 1; i <= n; i++) {	
			if (max != arr[1]) {	//가장많은 표를 받는게 다솜이가 아니다
				if (max == arr[i]) {	//가장 많은 표를 받는 녀석을 찾아서 하나 빼고 다솜이에게 줌 그리고 다시 가장 큰 놈을 찾으러
					arr[i] -= 1;
					arr[1] += 1;
					badman++;
					break;
				}
			} else {	//가장 많은 표를 받은 사람 중 다솜이가 있다.
				for (int i = 2; i <= n; i++) { 	
					if (arr[1] == arr[i]) {	//같은 표를 받은 사람 찾기
						arr[i] -= 1;
						arr[1] += 1;
						badman++;
						break;
					}
				}
				printf("%d", badman);
				return 0;
			}
		}
	}*/
}