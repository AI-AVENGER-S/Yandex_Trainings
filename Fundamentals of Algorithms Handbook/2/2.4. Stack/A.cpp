#include <iostream>
#include <stack>

using namespace std;

int main() {
    int t;
    cin >> t;
    stack<int> stack;

    while(t--) {
        int q;
        cin >> q;

        switch (q){
            case 1:
                int x;
                cin >> x;
                stack.push(x);
                cout << stack.top() << '\n';
                break;
            
            case 2:
                stack.pop();
                int res = stack.empty() ? -1 : stack.top();
                cout << res << '\n';
                break;
        }
    }

    return 0;
}