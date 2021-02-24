#include<cstdio>
#include<cstring>

using namespace std;
int n;
char arr[100];

char adrian[3] = { 'A', 'B', 'C' };
char bruno[4] = { 'B', 'A', 'B', 'C' };
char goran[6] = { 'C', 'C', 'A', 'A', 'B', 'B' };

int cnt_a = 0, cnt_b = 0, cnt_g = 0;
int max = -1;

int main() {
	scanf("%d", &n);
	
	getchar();
	for(int i= 0; i< 100; i++)
		scanf("%1c", &arr[i]);

	int j = 0;
	for (int i = 0; i < n; i++) {
		if (j == 3) {
			j = 0;
		}
		if (arr[i] == adrian[j]) {
			cnt_a++;
		}
		j++;
	}

	j = 0;
	for (int i = 0; i < n; i++) {
		if (j == 4) {
			j = 0;
		}
		if (arr[i] == bruno[j]) {
			cnt_b++;
		}
		j++;
	}

	j = 0;
	for (int i = 0; i < n; i++) {
		if (j == 6) {
			j = 0;
		}
		if (arr[i] == goran[j]) {
			cnt_g++;
		}
		j++;
	}

	if (max < cnt_a)
		max = cnt_a;
	if (max < cnt_b)
		max = cnt_b;
	if (max < cnt_g)
		max = cnt_g;

	printf("%d\n", max);

	if (cnt_a == cnt_b && cnt_b == cnt_g) {
		printf("Adrian\nBruno\nGoran");
	}
	else if (max == cnt_a && cnt_a == cnt_b)
		printf("Adrian\nBruno");
	else if (max == cnt_a && cnt_a == cnt_g)
		printf("Adrian\nGoran");
	else if (max == cnt_g && cnt_g == cnt_b)
		printf("Bruno\nGoran");
	else if(max == cnt_a)
		printf("Adrian");
	else if (max == cnt_b)
		printf("Bruno");
	else if (max == cnt_g)
		printf("Goran");



	
	return 0;
}