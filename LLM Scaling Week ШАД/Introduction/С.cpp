#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <limits>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int sx, sy;
    cin >> sx >> sy;
    sx--; 
    sy--;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }

    string s;
    cin >> s;


    long long infinity = numeric_limits<long long>::max();
    vector<vector<long long> > dp(n, vector<long long>(m, infinity));

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    char first_char = s[0];
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == first_char) {
                dp[r][c] = abs(r - sx) + abs(c - sy);
            }
        }
    }

    for (int k = 1; k < s.length(); ++k) {
        char prev_char = s[k - 1];
        char curr_char = s[k];

        vector<vector<long long> > new_dp(n, vector<long long>(m, infinity));

        if (curr_char == prev_char) {
            new_dp = dp;
            dp = new_dp;
            continue;
        }


        vector<vector<long long> > dist_grid(n, vector<long long>(m, infinity));
        queue<pair<int, int> > q;


        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                if (dp[r][c] != infinity) {
                    dist_grid[r][c] = dp[r][c];
                    q.push({r, c});
                }
            }
        }

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();
            int cr = curr.first;
            int cc = curr.second;

            for (int i = 0; i < 4; ++i) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    if (dist_grid[cr][cc] + 1 < dist_grid[nr][nc]) {
                        dist_grid[nr][nc] = dist_grid[cr][cc] + 1;
                        q.push({nr, nc});
                    }
                }
            }
        }

        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                if (grid[r][c] == curr_char) {
                    new_dp[r][c] = dist_grid[r][c];
                }
            }
        }

        dp = new_dp;
    }

    long long min_time = infinity;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            min_time = min(min_time, dp[r][c]);
        }
    }

    cout << min_time << "\n";

    return 0;
}