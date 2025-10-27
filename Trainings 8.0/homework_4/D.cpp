#include "../bits/stdc++.h"

#define all(x) x.begin(), x.end()

using namespace std;
using ll = long long;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<ll> a(n, 0);
    
    for(int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0, r = n - 1;
    int best_l = 0, best_r = 0;
    ll min_diff = pow(10, 9);
    int diff = a[l] - a[r];
    
    while (l < r) {
        if (abs(min_diff) > abs(diff)) {
            best_l = l;
            best_r = r;
            min_diff = diff;
        }
        if (diff > 0){
            r -= 1;
            diff -= a[r];
        } else if (diff < 0) {
            l += 1;
            diff += a[l];
        } else {
            break;
        }
        
    }
    cout << abs(min_diff) << ' ' << best_l + 1 << ' ' << best_r + 1 << '\n';

    return 0;
}