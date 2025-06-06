class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        t_gas, t_cost, start_ind, curr_gas = 0, 0, 0, 0

        for i in range(len(gas)):
            t_gas += gas[i]
            t_cost += cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                start_ind = i + 1

        return start_ind if t_gas >= t_cost else -1
        