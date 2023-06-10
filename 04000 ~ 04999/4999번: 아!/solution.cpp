// 백준 4999번 아!
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	string user, doctor;

	cin >> user >> doctor;
	if (user.length() >= doctor.length())
		cout << "go\n";
	else
		cout << "no\n";
	
	return 0;
}
