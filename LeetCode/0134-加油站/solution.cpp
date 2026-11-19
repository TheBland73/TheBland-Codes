#include <vector>
using namespace std;
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_gas = 0;
        long long total_cost = 0;
        int size = gas.size();
        int start = 0;
        int acc = 0;

        for (int i = 0; i < size; ++i){
            total_cost += cost[i];
            total_gas += gas[i];
            acc += gas[i] - cost[i];

            if (acc < 0){
                start = i + 1;
                acc = 0;
            }
        }
        return total_cost - total_gas > 0 ? -1 : start;
    }
};
