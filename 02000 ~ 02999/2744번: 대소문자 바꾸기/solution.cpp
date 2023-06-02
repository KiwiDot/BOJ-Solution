// 백준 2744번 대소문자 바꾸기
#include <iostream>
using namespace std;

int main()
{
	string word;
	cin >> word;

	for (int i = 0; i < word.size(); i++)
	{
		if (word[i] < 'a')
			word[i] = tolower(word[i]);
		else
			word[i] = toupper(word[i]);
	}

	cout << word << endl;

	return 0;
}
