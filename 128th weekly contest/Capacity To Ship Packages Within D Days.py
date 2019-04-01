class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        """
        背包问题的变形
        其实就是问你：有D个背包，若干物品，全部放入背包中，确定背包最小容量
        将搜索空间限制在min到right之间，如果mid满足，那么更新搜索空间为[min_cap,mid)，否则为[mid+1, max_cap]
        :param weights:
        :param D:
        :return:
        """
        min_cap, max_cap = max(weights), sum(weights)
        while min_cap < max_cap:
            mid, need_days, current_weight = int((min_cap + max_cap) / 2), 1, 0
            for w in weights:
                if current_weight + w > mid:
                    need_days += 1
                    current_weight = 0
                current_weight += w
            if need_days > D:
                min_cap = mid + 1
            else:
                max_cap = mid
        return min_cap
