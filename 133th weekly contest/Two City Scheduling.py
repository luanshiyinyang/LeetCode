class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(cost[0] for cost in sorted(costs, key=lambda x: x[0]-x[1])[:len(costs)//2]) + sum(cost[1] for cost in sorted(costs, key=lambda x: x[0]-x[1])[len(costs)//2:])