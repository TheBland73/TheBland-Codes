#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<long long> stk;
        long long res = 0;
        long long sign = 1;
        long long num = 0;
        int n = (int)s.size();

        for (int i = 0; i < n; i++) {
            char ch = s[i];

            if (ch >= '0' && ch <= '9') {
                num = num * 10 + (ch - '0');
            }
            else if (ch == '+' || ch == '-') {
                res += sign * num;
                num = 0;
                sign = (ch == '+') ? 1 : -1;
            }
            else if (ch == '(') {
                stk.push(res);
                stk.push(sign);
                res = 0;
                sign = 1;
                num = 0;
            }
            else if (ch == ')') {
                res += sign * num;
                num = 0;

                long long preSign = stk.top(); stk.pop();
                long long preRes = stk.top(); stk.pop();

                res = preSign * res + preRes;
                sign = 1;
            }
        }

        res += sign * num;
        return (int)res;
    }
};
