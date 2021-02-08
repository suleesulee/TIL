//보류.....


#define DEBUG 1

#if DEBUG
#include<cstdio>
#endif

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n, m;
int cur_channel = 100;
int remote[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
int channel[6] = { -1, -1, -1, -1, -1, -1};
vector<int> cha;
int min_move;

int move_possible(int num) {

	while (num) {
		if (find(remote, remote + 10, num % 10) != remote[9])
			return 1;

		if (num != 0) {
			num /= 10;
		}
	}

	return 0;
}

int num_digit(int num) {
	int digit = 0;

	while (1) {
		if (digit != 0) {
			if (num / 10 != 0) {
				num /= 10;
				digit++;
			}
			else {
				digit++;
				break;
			}
		}
		else {
			digit = 1;
			break;
		}
	}
	return digit;
}

int main() {

	cin >> n >> m;
	
	int tmp;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		
		for (int j = 0; j < 10; j++) {
			if (remote[j] == tmp)
				remote[j] = -1;
		}
	}

#if DEBUG
	printf("remote control : ");
	for (int i = 0; i < 10; i++)
		printf("%d", remote[i]);

	printf("\n");
#endif

	int i = 0;

	/* 1. 보려고 하는 채널의 버튼이 안고장나서 바로 눌러서 이동가능한 경우*/
	while (1)
	{
		if (n / 10 != 0) {
			channel[i] = n % 10;
			cha.push_back(n % 10);
			n = n / 10;
			i++;
		}
		else {
			channel[i] = n % 10;
			cha.push_back(n % 10);
			break;

		}
	}

#if DEBUG
	//array 사용시
	for (int i = 0; i < 6; i++) {
		printf("%d ", channel[i]);
	}
	printf("\n");

	//vector 사용시
	for (int i = 0; i < cha.size(); i++) {
		printf("%d ", cha[i]);
	}
	printf("\n");
#endif

	int chanel_cnt = 0;

	for (int i = 0;i < cha.size(); i++) {
		for (int j = 0; j < 10; j++) {
			if (cha[i] == remote[j])
				chanel_cnt++;
		}
	}

	if (chanel_cnt == cha.size()) {
		printf("%ld", cha.size());
		return 0;
	}

	/*2. 그냥 +-버튼으로 보려고하는 채널로 이동*/

	if (n < cur_channel) {
		min_move = cur_channel - n;
	}
	else if (n == cur_channel) {
		printf("0");
		return 0;
	}
	else
		min_move = n - cur_channel;

	/*3. 남아있는 리모컨의 값으로 이동하려는 채널의 근처 값으로 이동해서 해당 값까지 이동하는 방법*/
	// 남아있는 채널의 자리수에서.. -1 +1 하여 다 찾고 그 값까지 근사값과 빼가며 가장 작은 값을 구해야하는건가.. 
	// 재귀를 돌려야하나..
	// 남아있는값 P 자리수... 9개와 6자리..가 최대 9P6 약 8만

	int push = 0;

	for (int i = 0; i < 1000000; i++) {
		if (move_possible(i)) {
			push = abs(n - i);

			int digit = num_digit(i);

			push += digit;

			if (min_move > push) {
				min_move = push;
			}
		}
	}

	cout << push << endl;



	return 0;
}