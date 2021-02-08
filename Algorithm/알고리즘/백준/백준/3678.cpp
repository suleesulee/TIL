#include<cstdio>

using namespace std;

int ts;
int in;


int katan[100001];
int number[5] = { 0, };
int start = 9;
int sel;
int temp1, temp2;


void go(){
	katan[1] = 1;
	number[0]++;
	katan[2] = 2;
	number[1]++;
	katan[3] = 3;
	number[2]++;
	katan[4] = 4;
	number[3]++;
	katan[5] = 5;
	number[4]++;
	katan[6] = 2;
	number[1]++;
	katan[7] = 3;
	number[2]++;
	katan[8] = 1;
	number[0]++;

	for (int j = 2; j < 10001 - 8; j++) {
		int tmp = katan[j];
		
		temp1 = number[0];
		temp2 = 0;

		for (int k = 0; k < 2; k++) {
			for (int i = 1; i < 5; i++) {
				if (temp1 > number[i]) {
					if(number[i] ! = )
					temp1 = number[i];
					temp2 = i;
				}
			}
			katan[start] != tmp;
		}

	}


}




int main() {
	scanf("%d", &ts);




	for (int i = 0; i < ts; i++) {
		scanf("%d", &in);
	}


	return 0;
}