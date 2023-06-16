// 백준 5522번 카드 게임
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int A, answer;
	answer = 0;

	for (int i = 0; i < 5; i++)
	{
		cin >> A;
		answer += A;
	}

	cout << answer << "\n";
	
	return 0;
}
