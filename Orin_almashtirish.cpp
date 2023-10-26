#include <iostream>
#include <vector>
#include <algorithm>

int find_min_swaps_to_sort_asc(std::vector<int>& array) {
    int size = array.size();
    std::vector<std::pair<int, int>> array_positions;
    for (int i = 0; i < size; i++) {
        array_positions.push_back(std::make_pair(array[i], i));
    }
    std::sort(array_positions.begin(), array_positions.end());

    std::vector<bool> visited(size, false);
    int swaps_count = 0;
    for (int i = 0; i < size; i++) {
        if (visited[i]  || array_positions[i].second == i) {
            continue;
        }
        int cycle_size = 0;
        int j = i;
        while (!visited[j]) {
            visited[j] = true;
            j = array_positions[j].second;
            cycle_size++;
        }
        if (cycle_size > 0) {
            swaps_count += cycle_size - 1;
        }
    }
    return swaps_count;
}

int find_min_swaps_to_sort_desc(std::vector<int>& array) {
    int size = array.size();
    std::vector<std::pair<int, int>> array_positions;
    for (int i = 0; i < size; i++) {
        array_positions.push_back(std::make_pair(array[i], i));
    }
    std::sort(array_positions.rbegin(), array_positions.rend());

    std::vector<bool> visited(size, false);
    int swaps_count = 0;
    for (int i = 0; i < size; i++) {
        if (visited[i]  || array_positions[i].second == i) {
            continue;
        }
        int cycle_size = 0;
        int j = i;
        while (!visited[j]) {
            visited[j] = true;
            j = array_positions[j].second;
            cycle_size++;
        }
        if (cycle_size > 0) {
            swaps_count += cycle_size - 1;
        }
    }
    return swaps_count;
}

int minimum_swaps_to_minimize_adjacent_diff(std::vector<int>& arr) {
    std::vector<int> arr_copy_asc = arr;
    std::vector<int> arr_copy_desc = arr;
    int sorted_in_asc = find_min_swaps_to_sort_asc(arr_copy_asc);
    int sorted_in_desc = find_min_swaps_to_sort_desc(arr_copy_desc);
    return std::min(sorted_in_asc, sorted_in_desc);
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    std::cout << minimum_swaps_to_minimize_adjacent_diff(arr) << std::endl;
    return 0;
}
