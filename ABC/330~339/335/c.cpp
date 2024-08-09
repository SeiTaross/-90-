// c.pyを無理やりCPPに変換してもらってACしたもの

#include <iostream>
#include <deque>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    vector<vector<string>> query(Q, vector<string>(2));
    for (int i = 0; i < Q; ++i) {
        cin >> query[i][0];
        if (query[i][0] == "1") {
            cin >> query[i][1];
        } else {
            cin >> query[i][1];
        }
    }

    deque<pair<int, int>> dragon;
    for (int i = 1; i <= N; ++i) {
        dragon.push_back({i, 0});
    }

    for (const auto& q : query) {
        if (q[0] == "1") {
            char C = q[1][0];
            auto head = dragon.front();
            int head_x = head.first;
            int head_y = head.second;

            if (C == 'U') {
                ++head_y;
            } else if (C == 'D') {
                --head_y;
            } else if (C == 'R') {
                ++head_x;
            } else if (C == 'L') {
                --head_x;
            }
            dragon.pop_back();
            dragon.push_front({head_x, head_y});
        } else {
            int p = stoi(q[1]);
            cout << dragon[p - 1].first << " " << dragon[p - 1].second << endl;
        }
    }

    return 0;
}
