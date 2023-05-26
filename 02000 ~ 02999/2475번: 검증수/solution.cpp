// 백준 2475번 검증수
# define _CRT_SECURE_NO_WARNINGS
# include <stdio.h>

int main() {
	int num[5], answer;
	
	for (int i = 0; i < 5; i++)
		scanf("%d", &num[i]);

	answer = 0;
	for (int i = 0; i < 5; i++)
		answer += num[i] * num[i];
	printf("%d", answer % 10);

	return 0;
}
