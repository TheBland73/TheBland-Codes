#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> res(size,1); //空间为size，默认初始为1

        if (size == 1){
            return res;
        }

        for (int i = 1; i < size; ++i){
            res[i] = res[i-1] * nums[i-1];
        }

        int suffix = 1;
        for (int i = size-1; i >= 0; --i){
            res[i] = res[i] * suffix;
            suffix = suffix * nums[i];
        }
        return res;
    }
};
