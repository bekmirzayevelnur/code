#include <iostream>
#include <vector>

int main() {
    int a;
    std::cin >> a;
    std::string b;
    std::cin >> b;
    
    int s = 0;
    std::vector<int> arr;
    std::vector<int> arr1;
    int l = 0;
    int ml = 0;
    
    for (int i = 0; i < a; i++) {
        char character = b[i];
        if (character == '#') {
            if (s != 0) {
                arr.push_back(s);
                s = 0;
                l /= 2;
                arr1.push_back(ml - l + 1);
                l = 0;
            }
        } else {
            s += 1;
            l += 1;
            ml = i;
        }
    }
    
    int k = arr[0];
    int lk = 0;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > k) {
            k = arr[i];
            lk = i;
        }
    }
    
    std::cout << arr1[lk] << std::endl;
    
    return 0;
}
