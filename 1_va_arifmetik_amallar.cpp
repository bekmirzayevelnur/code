#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

int main() {
    int N;
    std::cin >> N;

    std::vector<int> dp(5001, 5001);
    dp[1] = 1;

    for (int i = 2; i <= N; i++) {
        for (int j = 1; j <= i / 2; j++) {
            dp[i] = std::min(dp[i], dp[j] + dp[i - j]);
        }

        int j = 1;
        while (j * j <= i) {
            if (i % j == 0) {
                dp[i] = std::min(dp[i], dp[i / j] + dp[j]);
            }
            j++;
        }
    }

    std::cout << dp[N] << std::endl;

    return 0;
}
