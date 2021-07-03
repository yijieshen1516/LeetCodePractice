
# Definition for an Interval.
import operator


class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule):
        # flatten schedule
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)

        # sort events by start
        events.sort(key=operator.attrgetter('start'))

        # collect result
        res = []
        iterator = iter(events)
        prev_end = next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res


schedule = [[[1,2], [5, 6]], [[1, 3]], [[4, 10]]]
print(Solution().employeeFreeTime(schedule))

