#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        int n = stations.size();
        int MaxLimit = startFuel;
        int i = 0, ans = 0;
        priority_queue<int> Q;

        while (1) {
            if (MaxLimit >= target)
                return ans;

            while (i < n && stations[i][0] <= MaxLimit) {
                Q.push(stations[i][1]);
                i++;
            }

            if (!Q.empty()) {
                MaxLimit += Q.top();
                Q.pop();
            } else {
                return -1;
            }

            ans++;
        }

        return ans;
    }
};

int main() {
    int target, startFuel, n;

    cout << "Enter target distance: ";
    cin >> target;

    cout << "Enter starting fuel: ";
    cin >> startFuel;

    cout << "Enter number of stations: ";
    cin >> n;

    vector<vector<int>> stations(n, vector<int>(2));

    cout << "Enter station position and fuel for each station:\n";
    for (int i = 0; i < n; i++) {
        cin >> stations[i][0] >> stations[i][1];
    }

    Solution obj;
    int result = obj.minRefuelStops(target, startFuel, stations);

    cout << "Minimum refueling stops: " << result << endl;

    return 0;
}