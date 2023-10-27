#include <iostream>
#include <string>

bool is_palindrome(const std::string& s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - 1 - i]) {
            return false;
        }
    }
    return true;
}

int find_smallest_non_palindromic_substring(const std::string& s) {
    int n = s.length();
    for (int length = 1; length <= n; length++) {
        for (int start = 0; start <= n - length; start++) {
            std::string substring = s.substr(start, length);
            if (!is_palindrome(substring)) {
                return length;
            }
        }
    }
    return -1;
}

int main() {
    int T;
    std::cin >> T;

    while (T--) {
        std::string S;
        std::cin >> S;
        int result = find_smallest_non_palindromic_substring(S);
        std::cout << result << std::endl;
    }

    return 0;
}
