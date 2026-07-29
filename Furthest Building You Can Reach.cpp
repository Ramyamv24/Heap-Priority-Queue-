#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& h, int b, int l) {

        // Max-heap to store brick usage
        priority_queue<int> p;

        int i = 0, diff = 0;

        for (i = 0; i < h.size() - 1; i++) {

            diff = h[i + 1] - h[i];

            if (diff <= 0) {
                continue;
            }

            b -= diff;
            p.push(diff);

            if (b < 0) {
                b += p.top();
                p.pop();
                l--;
            }

            if (l < 0)
                break;
        }

        return i;
    }
};

int main() {
    int n;
    cout << "Enter number of buildings: ";
    cin >> n;

    vector<int> heights(n);
    cout << "Enter building heights: ";
    for (int i = 0; i < n; i++) {
        cin >> heights[i];
    }

    int bricks, ladders;
    cout << "Enter number of bricks: ";
    cin >> bricks;

    cout << "Enter number of ladders: ";
    cin >> ladders;

    Solution obj;
    int ans = obj.furthestBuilding(heights, bricks, ladders);

    cout << "Furthest building index: " << ans << endl;

    return 0;
}