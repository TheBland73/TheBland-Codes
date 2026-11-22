#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        int slow = 0, fast = 0;

        //双指针前移覆盖
        //"  hello world  "
        while (fast < n){
            while (fast < n && s[fast] == ' ') fast++; //跳国连续空格
            if(fast >= n) break; //终止循环
            if(slow > 0) s[slow++] = ' '; //跳过首个单词，最后一个单词上面fast就会终止循环
            while (fast < n && s[fast] != ' ') s[slow++] = s[fast++];
        }
        s.resize(slow); //截断

        //整体翻转
        reverse(s.begin(), s.end());
        
        //逐个单词反转
        int start = 0;
        for(int k = 0; k <= slow; k++){
            if (s[k] == ' ' || k == slow){
                reverse(s.begin() + start ,s.begin() + k); //[ , )
                start = k + 1;
            }
        }
        return s;
    }
};
