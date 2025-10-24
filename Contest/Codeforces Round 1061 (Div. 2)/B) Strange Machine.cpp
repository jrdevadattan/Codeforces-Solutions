#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;
        string s;
        cin >> s;
        vector<long long> queries(q);
        for (int i = 0; i < q; i++) cin >> queries[i];

        bool hasB = false;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'B') hasB = true;
        }

        if (!hasB) {
            for (int i = 0; i < q; i++) {
                cout << queries[i] << endl;
            }
            continue;
        }

        vector<int> k(n), len(n), nxt(n);
        for (int i = 0; i < n; i++) {
            int j = 0;
            while (j < n) {
                int pos = (i + j) % n;
                if (s[pos] == 'B') break;
                j++;
            }
            k[i] = j;
            len[i] = j + 1;
            int bpos = (i + j) % n;
            nxt[i] = (bpos + 1) % n;
        }

        for (int qi = 0; qi < q; qi++) {
            long long a = queries[qi];
            long long time = 0;
            int pos = 0;
            while (a > 0) {
                if (a <= k[pos]) {
                    time += a;
                    a = 0;
                } else {
                    a = (a - k[pos]) / 2;
                    time += len[pos];
                    pos = nxt[pos];
                }
            }
            cout << time << endl;
        }
    }
    return 0;
}
