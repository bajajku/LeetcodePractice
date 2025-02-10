"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
no conflict:
    move forward

conflict:
    day += 1
    day of conflict new interval

in the end add +1 for last day.

"""

# 0,4, 5,10 15,20


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> bool:
        
        # a bit different approach from other interval questions

        '''
        So it goes like this we have start and end times of all meeting that we will 
        sort.

        Now we can keep count of meeting rooms needed at the current time

        How can we do this?
            -> so if start[s] < end[e], this means another meeting is being started before any
            meeting ended so we need another room ie. count += 1
            -> else: we can conclude a meeting ended so free the room, count -= 1

        Now since question ask for min number of day required,
        we need to keep count of max the count reached as this is minimum rooms we need
        so there is no conflicts.
        
        Drawing out makes much more sense but still a bit difficul;t in my opinion.
        '''
        startM = sorted([i.start for i in intervals])
        endM = sorted([i.end for i in intervals])

        res = 0
        count = 0

        s, e = 0, 0
        while s < len(startM) and e < len(endM):

            if(startM[s] < endM[e]):
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            res = max(res, count)

        return res






