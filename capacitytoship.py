class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def feasible(capacity):
            ndays = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    ndays += 1
                    if ndays > days:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(Solution().shipWithinDays(weights, days))