#include "../bits/stdc++.h"

#define all(x) x.begin(), x.end()

using namespace std;
using ll = long long;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    ll k;
    cin >> k;

    vector<int> a(n, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    vector<ll> diff(n + 1, 0); 
    for (int i = 0; i < m; ++i){
        int l, r;
        cin >> l >> r;
        diff[l - 1] += 1;     
        diff[r] -= 1;
    }

    vector<ll> impact(n);
    ll current_impact = 0;
    for (int i = 0; i < n; ++i) {
        current_impact += diff[i];
        impact[i] = current_impact;
    }

    ll total_discomfort = 0;
    for (int i = 0; i < n; ++i) {
        total_discomfort += (ll)a[i] * impact[i];
    }

    priority_queue<pair<ll, int>> pq;
    for (int i = 0; i < n; ++i) {
        if (a[i] > 0 && impact[i] > 0) {
            pq.push({impact[i], i});
        }
    }
    while (k > 0 && !pq.empty()) {
        pair<ll, int> top = pq.top();
        pq.pop();
        
        ll section_impact = top.first;
        int section_index = top.second;
        int brokes_on_section = a[section_index];

        ll repair_count = min((ll)brokes_on_section, k);

        total_discomfort -= repair_count * section_impact;
        
        k -= repair_count;
    }
    
    cout << total_discomfort << '\n';
    return 0;
}