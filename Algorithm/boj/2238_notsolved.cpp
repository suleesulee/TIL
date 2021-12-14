#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int u, n;
/*string s[100000];
int p[100000];

int no[100000];
int n_cnt = 0;
string res;
int cnt = 0;

int main() {
	memset(no, -1, sizeof(no));
	cin >> u >> n;

	for (int i = 0; i < n; i++) {
		cin >> s[i] >> p[i];
	}

	int min = 999999;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= n_cnt; j++) {
			if (p[i] == no[j]) {
				break;
			}
			else if (j == n_cnt) {	//no배열 끝까지 확인 
				//printf("0\n");
				if (min > p[i]) {
					//printf("1\n");
					min = p[i];
					res = s[i];
				}
				else if (min == p[i]) {
					//printf("2\n");
					no[n_cnt] = p[i];
					n_cnt++;
					min = 999999;
					i = 0;
				}
			}
		}
	}
	//for (int i = 0; i < n; i++) {
	//	printf("%d", no[i]);
	//}

	printf("%s %d", res.c_str(), min);
	return 0;
}*/

string s;
int p;
int res;
vector <pair<int, string>> v;
int main() {
	cin >> u >> n;
	for (int i = 0; i < n; i++) {
		cin >> s >> p;
		v.push_back(make_pair( p,s ));
	}
	
	sort(v.begin(), v.end());

	int tmp = v[0].first;
	for (int i = 1; i < n; i++) {
		if (tmp == v[i].first) {
			tmp = v[i].first;
			
		}
		else if (tmp != v[i].first) {	
			if (v[i].first != v[i + 1].first && i != 1)
			{
				res = i;
				break;
			}
			else if (i == 1) {
				res = 0;
				break;
			}
		}
	}

	cout << v[res].second<< " " << v[res].first;
}