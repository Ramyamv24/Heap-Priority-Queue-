#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        using T = tuple<int, int, int>;
        priority_queue<T, vector<T>, greater<T>> pq;

        int n = nums1.size(), m = nums2.size();

        // Push first element from nums2 paired with first min(k, n) elements of nums1
        for (int i = 0; i < min(k, n); i++) {
            pq.push({nums1[i] + nums2[0], i, 0});
        }

        vector<vector<int>> result;

        while (!pq.empty() && (int)result.size() < k) {
            auto [sum, i, j] = pq.top();
            pq.pop();

            result.push_back({nums1[i], nums2[j]});

            if (j + 1 < m) {
                pq.push({nums1[i] + nums2[j + 1], i, j + 1});
            }
        }

        return result;
    }
};

int main() {
    int n, m, k;

    cout << "Enter size of nums1: ";
    cin >> n;

    vector<int> nums1(n);
    cout << "Enter elements of nums1 (sorted): ";
    for (int i = 0; i < n; i++) {
        cin >> nums1[i];
    }

    cout << "Enter size of nums2: ";
    cin >> m;

    vector<int> nums2(m);
    cout << "Enter elements of nums2 (sorted): ";
    for (int i = 0; i < m; i++) {
        cin >> nums2[i];
    }

    cout << "Enter k: ";
    cin >> k;

    Solution obj;
    vector<vector<int>> ans = obj.kSmallestPairs(nums1, nums2, k);

    cout << "\nK Smallest Pairs:\n";
    for (auto &pair : ans) {
        cout << "[" << pair[0] << ", " << pair[1] << "]\n";
    }

    return 0;
}