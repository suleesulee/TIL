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

	//ū���� ������ ������ ���� 
	/*while (1) {
		for (int i = 1; i <= n; i++) {	//���� ���� ǥ�� �޴� ���� ����
			if (max < arr[i]) {
				max = arr[i];
			}
		}

		for (int i = 1; i <= n; i++) {	
			if (max != arr[1]) {	//���帹�� ǥ�� �޴°� �ټ��̰� �ƴϴ�
				if (max == arr[i]) {	//���� ���� ǥ�� �޴� �༮�� ã�Ƽ� �ϳ� ���� �ټ��̿��� �� �׸��� �ٽ� ���� ū ���� ã����
					arr[i] -= 1;
					arr[1] += 1;
					badman++;
					break;
				}
			} else {	//���� ���� ǥ�� ���� ��� �� �ټ��̰� �ִ�.
				for (int i = 2; i <= n; i++) { 	
					if (arr[1] == arr[i]) {	//���� ǥ�� ���� ��� ã��
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