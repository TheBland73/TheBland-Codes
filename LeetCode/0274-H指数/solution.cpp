#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        // sort(citations.begin(),citations.end());
        // reverse(citations.begin(),citations.end());
        int res = 0;
        sort(citations.begin(),citations.end(),greater<int>());  //大到小排列
        for (int val : citations)
            if (val >= res + 1){
                ++res;
            }
        return res;
    }
};
