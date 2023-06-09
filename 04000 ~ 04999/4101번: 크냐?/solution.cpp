// 백준 4101번 크냐?
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	long long a, b;

	while (true)
	{
		cin >> a >> b;
		if (a == 0 && b == 0)
			break;
		if (a > b)
			cout << "Yes\n";
		else
			cout << "No\n";
	}
	
	return 0;
}
