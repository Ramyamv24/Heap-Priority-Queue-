#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        int n = courses.size();
        if (n <= 0) return 0;

        // Swap duration and lastDay to sort by deadline
        for (int i = 0; i < n; i++) {
            swap(courses[i][0], courses[i][1]);
        }

        sort(courses.begin(), courses.end());

        priority_queue<int> q;
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += courses[i][1];
            q.push(courses[i][1]);

            if (sum > courses[i][0]) {
                sum -= q.top();
                q.pop();
            }
        }

        return q.size();
    }
};

int main() {
    int n;

    cout << "Enter number of courses: ";
    cin >> n;

    vector<vector<int>> courses(n, vector<int>(2));

    cout << "Enter duration and last day for each course:\n";
    for (int i = 0; i < n; i++) {
        cin >> courses[i][0] >> courses[i][1];
    }

    Solution obj;
    int result = obj.scheduleCourse(courses);

    cout << "Maximum number of courses that can be taken: " << result << endl;

    return 0;
}