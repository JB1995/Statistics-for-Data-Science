# Question 4: Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference.
# Goal_diff_count = GoalsFor - GoalsAgainst
class Solution4:
    def __init__(self, data):
        self.data = data
    def Goal_diff_count(self):
        self.data['GoalsFor'] = self.data['GoalsFor'].astype(int)
        self.data['GoalsAgainst'] = self.data['GoalsAgainst'].astype(int)
        self.data['GoalDiffCount'] = self.data['GoalsFor'] - self.data['GoalsAgainst']
        print('Solution 4:')
        print(self.data)
        print("Maximum Goal Difference: ", self.data['GoalDiffCount'].max())
        print("Minimum Goal Difference: ", self.data['GoalDiffCount'].min())
        return self.data