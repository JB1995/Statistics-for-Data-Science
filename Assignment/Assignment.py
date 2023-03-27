import pandas as pd
from Question1 import Solution1
from Question2 import Solution2
from Question3 import Solution3
from Question4 import Solution4
from Question5 import Solution5
from Question6 import Solution6

class Solution:
    #Question 1
    solution1 = Solution1()
    data = solution1.getdata()

    # Question 2
    solution2 = Solution2(data)
    data = solution2.startedPlaying()

    # Question 3
    solution3 = Solution3(data)
    data = solution3.top5teams()

    # Question 4
    solution4 = Solution4(data)
    data  = solution4.Goal_diff_count()

    # Question 5
    solution5 = Solution5(data)
    data = solution5.top5Winning()

    # Question 6
    solution6 = Solution6(data)
    data = solution6.groupByBestPosition()