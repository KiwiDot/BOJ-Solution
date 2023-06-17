// 백준 5597번 과제 안 내신 분..?
# define _CRT_SECURE_NO_WARNINGS
# include <stdio.h>

int main() {
	int n;
	int student[31] = {0,};
	
	for (int i = 0; i < 28; i++)
	{
		scanf("%d", &n);
		student[n] = 1;

	}

	for (int i = 1; i < 31; i++)
		if (not student[i])
			printf("%d\n", i);

	return 0;
}
