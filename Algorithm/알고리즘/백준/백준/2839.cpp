#include<cstdio>
int main() {
	int input;
	int cnt = 0;
	scanf("%d", &input);

	while (1) {
		if (input % 5 == 0) {
			cnt += input / 5;
			break;
		} else if(input >= 3){
			input = input - 3;
			cnt++;
			if (input == 0)
				break;
		} else {
			printf("-1");
			return 0;
		}
	}
	printf("%d", cnt);
	
	return 0;
}