#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<string> hs = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"};
    vector<string> ms = vector<string>(hs.begin(), hs.begin()+13);
    ms.insert(ms.end(), {"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"});

    int h, m;
    cin >> h >> m;

    if (m == 0) {
        cout << hs[h] << " o' clock";
    } else if (m == 1) {
        cout << "one minute past " << hs[h];
    } else if (m == 15) {
        cout << "quarter past " << hs[h];
    } else if (m <= 20) {
        cout << ms[m] << " minutes past " << hs[h];
    } else if (m < 30) {
        cout << "twenty " << ms[m-20] << " minutes past " << hs[h];
    } else if (m == 30) {
        cout << "half past " << hs[h];
    } else {
        m = 60 - m;
        if (m == 1) {
            cout << "one minute to " << hs[h+1];
        } else if (m == 15) {
            cout << "quarter to " << hs[h+1];
        } else if (m <= 20) {
            cout << ms[m] << " minutes to " << hs[h+1];
        } else if (m < 30) {
            cout << "twenty " << ms[m-20] << " minutes to " << hs[h+1];
        }
    }

    return 0;
}
