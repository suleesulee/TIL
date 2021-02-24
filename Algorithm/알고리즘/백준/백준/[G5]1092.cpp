#include<cstdio>
#include<cstdlib>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int n, m;
vector<int> box;

int res;
int cnt = 0;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	scanf("%d", &n);
	int limit[n];

	for (int i = 0; i < n; i++) {
		scanf("%d", &limit[i]);
	}

	cin >> m;

	int tmp;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		box.push_back(tmp);
	}

	sort(limit, limit + n, desc);
	sort(box.begin(), box.end(), desc);

	if (box.front() > limit[0])
		printf("-1");
	else {
		while(1){
			for (int i = 0; i < n ; i++) {
				for (int j = 0; j < box.size(); j++)
					if (limit[i] >= box[j]) {
						box.erase(box.begin() + j);
						break;
					}
			}
			cnt++;
	
			if (box.size() == 0) {
				break;
			}
		}

		cout << cnt << endl;
	}

	return 0;
}

/* 
백준 랭크 골드5

그리디 알고리즘문제라고 한다. 

일단 문제를 푸는 방식은 맞게 세웠다.

1. 받아서 정렬한다.

2. 박스 중 가장 무거운 것의 무게가 크레인이 견딜수있는 무게보다 크면 -1 로 종료

3. for문을 돌면서 한 크레인씩 비교해서 내려가며 박스를 치우면 배열값을 -1로 바꾸고 진행... 한바퀴 돌면 1회돌았다고 생각하여 cnt값 올려주기

4. 박스배열이 모두 -1이라면 다 돈거라고 생각하여 횟수 찍고 종료

구현 중 생긴 문제점

일단 박스와 크레인 값을 모두 배열로 놓고 비교하려하니깐 치웠던 박스의 값을 -1로 바꾸고 비교해 나가는 과정 때문에 for문이 복잡해졌다.

(찾아보니 이 문제는 배열로 해결하려하면 시간초과가 발생한다고 한다.)

그래서 이 방법이 맞는것인지 잘 된 풀이를 찾아봤는데 푸는 방식은 맞았다.

다만 sort 함수를 내림차순으로 이용하는 것이 문제를 푸는데 직관적이었고 sort 함수의 내림차순관련해서 하는 방법을 몰라 

검색해서 도움을 얻었다. 해당 부분을 반드시 암기하자.

상자 관련 변수를 vector로 변경하여 진행하니 코드가 간결해졌다. 치운 상자를 삭제해버리니 비교하는 것도 줄어들었다.

벡터관련해서 자주 사용하지 않다보니 어느순간 관련 메소드에 대해서 당황하는데 기본적인 부분이니 익숙해지도록 해야한다.

또한 c의 입출력과 c++의 입출력을 혼용해서 쓰는데 주력언어로 c만 사용해서인지 c++로 값을 받는 부분이 좀 불편한 느낌..

연습하자.. 브실골플 까지는 노력으로 할수있는 부분이라고 생각한다.
*/