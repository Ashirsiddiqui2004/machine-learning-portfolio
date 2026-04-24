#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        int ones = 0;
        for (char c : s) if (c == '1') ones++;

        // All zeros case
        if (ones == 0) {
            if (n == 1) cout << 1 << "\n";
            else cout << (n - 1) / 2 << "\n";
            continue;
        }

        int extra = 0;

        for (int i = 0; i < n; ) {
            if (s[i] == '1') {
                i++;
                continue;
            }

            int j = i;
            while (j < n && s[j] == '0') j++;
            int L = j - i;

            // This segment has at least one adjacent '1'
            extra += (L - 1) / 2;

            i = j;
        }

        cout << ones + extra << "\n";
    }

    return 0;
}
