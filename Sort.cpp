#include <bits/stdc++.h>

using namespace std;

bool solishtir(string s1, string s2)

{

    int s1l = s1.length(), s2l = s2.length();

    if (s1l != s2l)

        return s1l < s2l;

    return s1 < s2;

}

int main()

{

    vector<string> vec;

    string son;

    int n;

    cin >> n;

    for (int i = 0; i < n; i++)

    {

        cin >> son;

        vec.push_back(son);

    }

    sort(vec.begin(), vec.end(), solishtir);

    for (auto i : vec)

    {

        cout << i << endl;

    }

}
