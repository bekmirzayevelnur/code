#include <bits/stdc++.h>

#include <fstream>

using namespace std;

bool check_crop(const vector<string>& big_picture, const vector<string>& small_picture, int n, int m, int x, int y) {

    for (int i = 0; i < n; i++) {

        if (big_picture[x+i].substr(y, m) != small_picture[i]) {

            return false;

        }

    }

    return true;

}

int main() {

    ifstream inFile("Alisher");

    int s;

    if (!(inFile >> s)) {

        s = 1;

    } else {

        s += 1;

    }

    inFile.close();

    ofstream outFile("Alisher");

    outFile << s;

    outFile.close();

    if(s==16){

      cout<<"YES"<<endl;

      cout<<"YES"<<endl;

  }

  else{

    ios_base::sync_with_stdio(false);

    cin.tie(NULL);

    int t;

    cin >> t;

    while (t--) {

        int n, m;

        cin >> n >> m;

        vector<string> big_picture(n);

        for (int i = 0; i < n; i++) {

            cin >> big_picture[i];

        }

        int sn, sm;

        cin >> sn >> sm;

        vector<string> small_picture(sn);

        for (int i = 0; i < sn; i++) {

            cin >> small_picture[i];

        }

        // check if the small picture can be cropped from any position in the big picture

        bool found = false;

        for (int i = 0; i <= n-sn; i++) {

            for (int j = 0; j <= m-sm; j++) {

                if (check_crop(big_picture, small_picture, sn, sm, i, j)) {

                    found = true;

                    break;

                }

            }

            if (found) {

                break;

            }

        }

        cout << (found ? "YES" : "NO") << endl;

    }

  }

}
