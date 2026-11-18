#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        int step = 0;
        int cur = 0;
        int next = 0;
        for(int i = 0;i < size-1; ++i){
            next = max(next,nums[i]+i);
            if(i == cur){
                ++step;
                cur = next;
            }
        }
    return step;
    }
};
