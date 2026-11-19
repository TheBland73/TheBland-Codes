from typing import List
#常规想法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        profit = [0] * size

        for i in range(size):
            profit[i] = gas[i] - cost[i]

        #特殊情况判断
        if size == 1:
            if profit[0] >= 0:
                return 0
            else:
                return -1

        for idx,val in enumerate(profit):
            flag = 1
            gas_total = val
            # if val >= 0 and profit[(idx+1)%size] >= 0:
            #     print(f"{idx}被跳过")
            #     continue
            if val > 0:
                loc = idx + 1
                while loc % size != idx:
                    gas_total += profit[(loc % size)]
                    loc = (loc + 1) % size
                    if gas_total < 0:
                        flag = 0
                        break
                if flag:
                    return idx
        return -1

#贪心想法
# 这个题有一个非常经典的 O(n) 贪心 结论：

# 若 sum(gas) >= sum(cost)，则恰好存在一个合法起点；并且可以一次遍历找到它：
# 维护当前油箱 tank，一旦 tank < 0，说明起点不可能在 [start, i] 之间，直接把 start = i + 1，tank = 0。
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        size = len(gas)
        start, acc = 0, 0

        if total_cost > total_gas:
            return -1
        for i in range(size):
            acc += gas[i] - cost[i]
            if acc < 0:
                start, acc = i+1, 0
        return start


        


solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
# # print(solution.canCompleteCircuit([2,3,4],[3,4,3]))
# # print(solution.canCompleteCircuit([2],[2]))
# print(solution.canCompleteCircuit([2],[3]))
                

                

        
