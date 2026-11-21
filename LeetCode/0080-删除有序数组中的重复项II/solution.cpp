//KEY!!!：比起原地删除什么，更值得你关心的是你原地保留了什么

#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int size = nums.size();
        if (size <= 2){
            return size;
        }

        int cnt = 0;
        int prev = 0;
        for(int j = 0; j<size; ++j){
            if (j > 0 and prev == nums[j]){
                cnt += 1;
            }
            else{
                cnt = 1;
                prev = nums[j];
            }

            if (cnt <= 2){
                nums[i] = nums[j];
                ++i;
            }
        }
        return i;
    }
};
