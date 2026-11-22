#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
// 第一趟：正向扫描，算出最终有效边界（确定从哪里开始倒着填） // 第二趟：反向双指针，一次性把元素填好，没有重复平移
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        //[1,0,2,3,0,4,5,0,6,7,8,9,10,11,12,13]
        //   i     i     i
        //[1,0,0,2,3,0,0,4,5,0,0,6,7 ,8 ,9 ,10]
        //   i       i       i

        //[1,0,2,0,2]
        //[1,0,0] l=2,r=1
        int size = arr.size();
        int left = 0,right = size-1;
        while(left < right){
            if(arr[left] == 0){
                right--;
            }
            left++;
        }

        int l = right;
        int r = size-1;
        if(arr[l] == 0 && left == right){   //判断是否是0截断边界
            arr[r] = 0;  //提前置0
            r--;
            l--;
        }
        while (l>=0){
            if(arr[l] == 0){
                arr[r--] = 0;
                arr[r--] = 0;
                l--;
            }
            else{
                arr[r--] = arr[l--];
            }
        }
    }
};


int main() {
   Solution sol;
   vector<int>arr = {1,0,2,3,0,4,5,0};
   sol.duplicateZeros(arr);

   return 0;
}



// #include <algorithm>
// #include <iostream>
// #include <vector>
// using namespace std;

// class Solution {
// public:

//     void duplicateZeros(vector<int>& arr) {
//         int size = arr.size();
//         int slow = 0, fast = 0;

//         while (fast < size){
//             if(arr[fast] == 0 && fast+1 < size){
//                 for(int i = size-1; i >= fast+1; i--){
//                     arr[i] = arr[i-1];
//                 }
//                 arr[fast+1] = 0;
//                 fast += 2;
//             }
//             else{
//                 ++fast;
//             }
//         }
        
//         for (int val: arr){
//             cout << val << ' ';
//         }
//     }
// };
